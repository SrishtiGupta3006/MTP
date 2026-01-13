#!/usr/bin/env python3
"""
output_strict_parallel.py
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Source.strict_parallel import StrictParallelEnforcer
from helper.dfa_definitions import (
    Strict_parallel_phi1,
    Strict_parallel_phi2
)

# Load property DFAs
phi1 = Strict_parallel_phi1()
phi2 = Strict_parallel_phi2()

enforcer = StrictParallelEnforcer([phi1, phi2])

print("\n=== Strict Parallel Enforcer ===")
print("Valid inputs: r, l, f, b, s")
print("Type 'end' to stop\n")

while True:
    a = input("Input event: ").strip()

    if a == "end":
        print("\nStopping execution.")
        break

    if a not in ['r','l','f','b','s']:
        print("Invalid input.")
        continue

    released = enforcer.step(a)

    print("Released output :", released)
    print("Current states  :", enforcer.q)
    print("Global output   :", enforcer.output)
    print("-" * 50)
