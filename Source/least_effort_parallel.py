#!/usr/bin/env python3
"""
least_effort_parallel.py
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helper.product import DFA

class LeastEffortParallelEnforcer:

    def __init__(self, enforcers):
        self.enforcers = enforcers
        self.n = len(enforcers)

        # current DFA states + candidate buffers
        self.q = [dfa.q0 for dfa in enforcers]
        self.candidate = [[] for _ in enforcers]

        self.output = []

    def process_event(self, a):

        # appending event to each enforcer's buffer
        for i in range(self.n):
            self.candidate[i].append(a)

        safe_sequences = []

        for i, dfa in enumerate(self.enforcers):
            if dfa.is_safe(self.q[i], self.candidate[i]):
                safe_sequences.append((i, self.candidate[i].copy()))

        # if any enforcer can release
        if safe_sequences:
            released = []

            # OR-merge: maintain order, avoid duplicates
            for idx, seq in safe_sequences:
                for sym in seq:
                    if sym not in released:
                        released.append(sym)

            # appending to global output
            self.output.extend(released)

            # updating DFA states and reset local buffers
            for i in range(self.n):
                self.q[i] = self.enforcers[i].next_state(self.q[i], self.candidate[i])
                self.candidate[i] = []

            return released

        return []

    def get_output(self):
        return self.output


# Optional alias
def least_effort_parallel(enforcers):

    return LeastEffortParallelEnforcer(enforcers)
