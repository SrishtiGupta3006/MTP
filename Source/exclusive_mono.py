#!/usr/bin/env python3
"""
exclusive_mono.py
"""

class ExclusiveMonolithicEnforcer:

    def __init__(self, dfa):

        self.dfa = dfa
        self.q = dfa.q0          # committed state
        self.sigma_c = []        # buffer σ_c
        self.output = []         # global output

    def _compute_tentative_state(self):
       
        temp = self.q
        for a in self.sigma_c:
            temp = self.dfa.d(temp, a)
            if temp is None:
                break
        return temp

    def step(self, a):

        # Safety check
        if a not in self.dfa.S:
            raise ValueError(f"Invalid input symbol: {a}")
        
        # Append event to buffer
        self.sigma_c.append(a)

        temp_state = self.q

        # Scan prefixes of σ_c
        for i, sym in enumerate(self.sigma_c):
            temp_state = self.dfa.d(temp_state, sym)

            if temp_state is None:
                break

            # Accepting prefix found
            if self.dfa.F(temp_state):
                released = self.sigma_c[:i+1]

                # Commit state
                self.q = temp_state

                # Clear buffer
                self.sigma_c = []

                # Save output
                self.output.extend(released)

                return released

        return []

    def enforce(self, input_word):

        # Enforce a complete input trace.
        out = []
        for a in input_word:
            released = self.step(a)
            if released:
                out.extend(released)
        return out

    def reset(self):
        
        # Reset enforcer state.
        self.q = self.dfa.q0
        self.sigma_c = []
        self.output = []

    def debug_state(self):

        return self._compute_tentative_state(), self.q
