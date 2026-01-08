#!/usr/bin/env python3
"""
output_LE_mono.py
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from helper.dfa_definitions import LE_mono_phi1, LE_mono_phi2
from Source.least_effort_mono import least_effort_monolithic_enforcer


phi1 = LE_mono_phi1()
phi2 = LE_mono_phi2()

# Least Effort Monolithic Enforcer (OR-Product) ------------------------
enforcer_fn = least_effort_monolithic_enforcer("OR_Product", phi1, phi2)

running_output = []

print("Enter actions one by one (r, l, f, b, s). Type 'end' to finish.\n")

while True:
    action = input("Next action: ").strip().lower()

    if action == "end":
        # Releasing the remaining buffer
        remaining = enforcer_fn(None)
        if remaining:
            running_output.extend(remaining)
        print("\nStopped input. Final output sequence:")
        print(running_output)
        break

    if action not in ['r', 'l', 'f', 'b', 's']:
        print("Invalid action! Please enter r, l, f, b, s or 'end'.")
        continue
    
    released, buffer_snapshot = enforcer_fn(action, debug=True)
    print("Buffer (not yet released):", buffer_snapshot)

    if released:
        running_output.extend(released)

    print("Running output so far:", running_output)
    print("-" * 50)
