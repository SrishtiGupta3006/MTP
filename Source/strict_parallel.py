#!/usr/bin/env python3
"""
Strict Parallel Enforcer
Algorithm 3 (Paper)
"""

class StrictParallelEnforcer:
    def __init__(self, dfas):
        """
        dfas: list of DFAs (phi1, phi2, ..., phik)
        """
        self.dfas = dfas
        self.k = len(dfas)

        # current DFA states
        self.q = [dfa.q0 for dfa in dfas]

        # output trace
        self.output = []

    def step(self, a):
        """
        Process one input event a.
        Returns released event or [].
        """

        next_states = []

        # advance all DFAs in parallel
        for i, dfa in enumerate(self.dfas):
            qi = self.q[i]
            qi_next = dfa.d(qi, a)

            # if any DFA blocks → suppress output
            if qi_next is None:
                return []

            next_states.append(qi_next)

        # all transitions valid → commit states
        self.q = next_states

        # strict semantics: event is released
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
