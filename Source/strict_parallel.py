#!/usr/bin/env python3
"""
Strict Parallel Enforcer

"""

class StrictParallelEnforcer:
    def __init__(self, dfas):

        self.dfas = dfas
        self.k = len(dfas)

        # current DFA states
        self.q = [dfa.q0 for dfa in dfas]

        # output trace
        self.output = []

    def step(self, a):

        next_states = []

        # advance all DFAs in parallel
        for i, dfa in enumerate(self.dfas):
            qi = self.q[i]
            qi_next = dfa.d(qi, a)

            if qi_next is None:
                return []

            next_states.append(qi_next)

        self.q = next_states

        self.output.append(a)
        return [a]

    def enforce(self, input_word):
        out = []
        for a in input_word:
            out.extend(self.step(a))
        return out

    def reset(self):
        self.q = [dfa.q0 for dfa in self.dfas]
        self.output = []
