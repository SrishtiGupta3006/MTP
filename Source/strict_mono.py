# Source/strict_mono.py

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helper.product import product_and


class StrictMonolithicEnforcer:

    def __init__(self, dfas, name="StrictMonolithic"):
        assert isinstance(dfas, list) and len(dfas) > 0, "No DFAs provided"

        # Build product DFA φ1 ∧ φ2 ∧ ... ∧ φn
        combined = dfas[0]
        for i in range(1, len(dfas)):
            combined = product_and(combined, dfas[i], name)

        self.dfa = combined

        # Current DFA state and buffer
        self.q = self.dfa.q0
        self.sigma_c = []

        self.output = []

    def step(self, a):
        
        # 1. Advance product DFA by ONE event
        self.q = self.dfa.d(self.q, a)

        # 2. Buffer the event
        self.sigma_c.append(a)

        # 3. If accepting → release buffer
        if self.dfa.F(self.q):
            released = self.sigma_c.copy()
            self.output.extend(released)
            self.sigma_c.clear()
            return released

        # Otherwise, block
        return []
