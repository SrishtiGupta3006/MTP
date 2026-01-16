#!/usr/bin/env python3
"""
exclusive_parallel.py
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from helper.Automata import DFA


# --------------------------------------------------
# DFA utilities
# --------------------------------------------------

def dfa_run(dfa: DFA, q, word):
    """
    Run DFA from state q over a word (list of symbols).
    Returns the resulting state.
    """
    for a in word:
        q = dfa.d(q, a)
    return q


def dfa_accepts_from(dfa: DFA, q, word):
    """
    Check whether DFA accepts when starting from state q

    Returns:
        (accepts: bool, q_end: state)
    """
    q_end = dfa_run(dfa, q, word)
    return dfa.F(q_end), q_end


# --------------------------------------------------
# Exclusive Parallel Enforcer
# --------------------------------------------------

class ExclusiveParallelEnforcer:
    def __init__(self, dfa_list):
        
        # Initialize the exclusive parallel enforcer.

        self.dfas = dfa_list
        self.n = len(dfa_list)

        # q_i : DFA state after all events in σs_i
        self.q = [dfa.q0 for dfa in self.dfas]

        # σc_i : local pending buffer (not yet accepted)
        self.sigma_c = [[] for _ in range(self.n)]

        # σs_i : locally accepted output (accumulating)
        self.sigma_s = [[] for _ in range(self.n)]

    def reset(self):
        # Reset all enforcers to initial configuration.
        self.q = [dfa.q0 for dfa in self.dfas]
        self.sigma_c = [[] for _ in range(self.n)]
        self.sigma_s = [[] for _ in range(self.n)]

    def step(self, a):

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

        # Local update for each enforcer
        for i in range(self.n):
            dfa = self.dfas[i]
            qi = self.q[i]
            buf = self.sigma_c[i]

            # Candidate chunk: σc_i · a
            word = buf + [a]

            accepts, q_end = dfa_accepts_from(dfa, qi, word)

            if accepts:
                # Locally accepted:
                #   append to σs_i
                #   clear σc_i
                #   advance DFA state
                self.sigma_s[i].extend(word)
                self.sigma_c[i] = []
                self.q[i] = q_end
            else:
                # Still unsafe — keep buffering
                self.sigma_c[i] = word

            # Collect debug info after local step
            debug_info.append({
                "enforcer": i + 1,
                "σc": list(self.sigma_c[i]),
                "σs": list(self.sigma_s[i]),
                "state": self.q[i],
            })

        # --------------------------------------------
        # GLOBAL RELEASE OPTIMIZATION
        # --------------------------------------------

        if all(len(c) == 0 for c in self.sigma_c):
            output = list(self.sigma_s[0])  # representative output

            # Clear σs after global release
            for i in range(self.n):
                self.sigma_s[i] = []

            return output, debug_info

        return [], debug_info

    def enforce(self, input_word):
        """
        Process a complete input word and return the enforced output.
        """
        out = []
        for a in input_word:
            emitted, _ = self.step(a)
            if emitted:
                out.extend(emitted)
        return out
