#!/usr/bin/env python3
"""
output_strict_serial.py
Runtime simulation for Strict Serial Enforcer (Algorithm 2)
"""

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from Source.strict_serial import StrictSerialEnforcer
from helper.dfa_definitions import get_all_Strict_serial_dfas

# Load ALL property DFAs
dfas = get_all_Strict_serial_dfas()

enforcer = StrictSerialEnforcer(dfas)

print("\n=== Strict Serial Enforcer ===")
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
    print("Buffers (σc)    :", enforcer.sigma_c)
    print("Global output   :", enforcer.output)
    print("-" * 50)
