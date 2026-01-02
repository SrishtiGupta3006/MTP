#!/usr/bin/env python3
"""
output_strict_mono.py
"""

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from Source.strict_mono import StrictMonolithicEnforcer
from helper.dfa_definitions import get_all_Strict_mono_dfas

# Load ALL DFAs
dfas = get_all_Strict_mono_dfas()

enforcer = StrictMonolithicEnforcer(dfas)

print("\n=== Strict Monolithic Enforcer ===")
print("Valid inputs: r, l, f, b, s")
print(f"Loaded {len(dfas)} DFAs")
print("Type 'end' to stop\n")

while True:
    a = input("Input event: ").strip()

    if a == "end":
        print("\nStopping execution.")
        break

    if a not in ['r', 'l', 'f', 'b', 's']:
        print("Invalid input.")
        continue

    released = enforcer.step(a)

    print("Released output :", released)
    print("Buffer (σc)     :", enforcer.sigma_c)
    print("Global output   :", enforcer.output)
    print("-" * 50)
