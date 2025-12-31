#!/usr/bin/env python3
"""
output_LE_parallel.py

Interactive simulation of Least Effort Parallel Enforcer
(OR of all enforcer outputs).
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from helper.dfa_definitions import (
    LE_parallel_phi1,
    LE_parallel_phi2,
    LE_parallel_phi3
)
from Source.least_effort_parallel import LeastEffortParallelEnforcer

# Load DFAs


enforcers = [
    LE_parallel_phi1(),
    LE_parallel_phi2(),
    LE_parallel_phi3()
]

le_parallel_enforcer = LeastEffortParallelEnforcer(enforcers)

print("Enter actions one by one (r, l, f, b, s, u, d). Type 'end' to finish.\n")
running_output = []

while True:
    action = input("Next action: ").strip().lower()

    if action == "end":
        print("\nStopped input. Final output sequence:")
        print(running_output)
        break

    if action not in ['r','l','f','b','s','u','d']:
        print("Invalid action! Please enter r, l, f, b, s, u, d or 'end'.")
        continue

    released_sequence = le_parallel_enforcer.process_event(action)

    if released_sequence:
        running_output.extend(released_sequence)

    print("Running output so far:", running_output)

    for idx, _ in enumerate(le_parallel_enforcer.enforcers):
        print(f"Enforcer {idx+1} buffer:",
              le_parallel_enforcer.candidate[idx])

    print("-" * 50)
