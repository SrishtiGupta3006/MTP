#!/usr/bin/env python3
"""
exclusive_parallel.py

Your desired semantics (accumulating σs and global release when all match):

- σc_i: pending buffer per enforcer i
- σs_i: persistent "output-so-far" per enforcer i (accumulates accepted chunks)
- At each input event a:
    if δ'*(q_i, σc_i·a) ∈ F'_i:
        q_i ← δ'*(q_i, σc_i·a)
        σs_i ← σs_i · (σc_i·a)     # accumulate
        σc_i ← ε
    else:
        σc_i ← σc_i·a

- Global release rule (WHAT YOU WANT):
    If all σs_i are identical, emit ONLY the new suffix that hasn't been globally emitted yet.

This is compatible with output_exclusive_parallel.py (same class name, step() signature,
and debug keys). It intentionally differs from Algorithm 7's step-proposal σs semantics.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from helper.Automata import DFA


def dfa_run(dfa: DFA, q, word):
    for a in word:
        q = dfa.d(q, a)
    return q


def dfa_accepts_from(dfa: DFA, q, word):
    q_end = dfa_run(dfa, q, word)
    return dfa.F(q_end), q_end


class ExclusiveParallelEnforcer:
    def __init__(self, dfa_list):
        self.dfas = dfa_list
        self.n = len(dfa_list)

        # qi: state reached by events that have been locally accepted & appended into σs_i
        self.q = [dfa.q0 for dfa in self.dfas]

        # σc_i: pending (not yet locally accepted)
        self.sigma_c = [[] for _ in range(self.n)]

        # σs_i: persistent "output so far" per enforcer (what you want to see/compare)
        self.sigma_s = [[] for _ in range(self.n)]

    def reset(self):
        self.q = [dfa.q0 for dfa in self.dfas]
        self.sigma_c = [[] for _ in range(self.n)]
        self.sigma_s = [[] for _ in range(self.n)]

    def step(self, a):
        """
        Process one event a and return (output_list, debug_info_list).

        Debug keys match your driver:
          { "enforcer": i+1, "σc": [...], "σs": [...], "state": qi }
        """

        # Optional snapshot if caller passes empty string
        if a == "":
            debug_info = []
            for i in range(self.n):
                debug_info.append({
                    "enforcer": i + 1,
                    "σc": list(self.sigma_c[i]),
                    "σs": list(self.sigma_s[i]),
                    "state": self.q[i],
                })
            return [], debug_info

        debug_info = []

        # ----------------------------
        # Local update for each enforcer
        # ----------------------------
        for i in range(self.n):
            dfa = self.dfas[i]
            qi = self.q[i]
            buf = self.sigma_c[i]

            word = buf + [a]  # σc_i · a
            accepts, q_end = dfa_accepts_from(dfa, qi, word)

            if accepts:
                # Locally accept the buffered chunk and append to persistent σs_i
                self.sigma_s[i].extend(word)
                self.sigma_c[i] = []
                self.q[i] = q_end
            else:
                # Keep buffering
                self.sigma_c[i] = word
                # qi unchanged, sigma_s unchanged

            debug_info.append({
                "enforcer": i + 1,
                "σc": list(self.sigma_c[i]),
                "σs": list(self.sigma_s[i]),
                "state": self.q[i],
            })

        # ----------------------------
        # ----------------------------
        # Global release: when all σs_i match
        # If yes: emit the whole σs and CLEAR σs for all
        # ----------------------------
        all_equal = True
        ref = self.sigma_s[0]
        for i in range(1, self.n):
            if self.sigma_s[i] != ref:
                all_equal = False
                break

        if all_equal and ref:
            output = list(ref)

            # Clear σs after global release (your requirement)
            for i in range(self.n):
                self.sigma_s[i] = []

            # Also reset global pointer (not needed anymore, but safe)
            self.global_emitted_len = 0
        else:
            output = []

        return list(output), debug_info


    def enforce(self, input_word):
        out = []
        for a in input_word:
            emitted, _ = self.step(a)
            if emitted:
                out.extend(emitted)
        return out
