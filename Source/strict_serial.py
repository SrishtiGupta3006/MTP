#!/usr/bin/env python3
"""
strict_serial.py
"""

import sys
sys.path.append("..")

from Source.Enforcer import enforcer


def serial_enforcer(name, *D):
    """
    Strict Serial Enforcer:
    Input → DFA1 → DFA2 → ... → DFAn
    """

    def serial_apply(sigma):
        assert len(D) > 0, "No DFAs provided."

        current_output = list(sigma)
        individual_outputs = {}

        for i, dfa in enumerate(D):
            dfa_name = getattr(dfa, 'name', f"Property_{i}")

            # ✅ buffer size = number of DFA states
            buffer_size = len(dfa.Q)

            current_output = enforcer( dfa, current_output, maxBuffer=buffer_size)

            if current_output is None:
                current_output = []

            individual_outputs[dfa_name] = current_output.copy()

        return current_output, individual_outputs

    return serial_apply


# Optional alias
def strict_serial(name, *D):
    return serial_enforcer(name, *D)
