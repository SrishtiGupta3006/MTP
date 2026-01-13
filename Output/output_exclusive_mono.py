#!/usr/bin/env python3
"""
output_exclusive_mono.py
"""

import sys
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)
sys.path.append(PROJECT_ROOT)

from helper.product import product
from helper.exclusive_modified_automata import get_all_exclusive_modified
from Source.exclusive_mono import ExclusiveMonolithicEnforcer


# Build Exclusive Monolithic Enforcer (n-ary, automatic)
mods = get_all_exclusive_modified()
A_and = product(*mods, "Exclusive_Mono")
enforcer = ExclusiveMonolithicEnforcer(A_and)

print("\n=== Exclusive Monolithic Enforcer ===")
print("Valid inputs: [ f, l, o, n, r ]")
print("Type 'end' to stop\n")

while True:
    a = input("Input event: ").strip()

    if a == "end":
        print("\nStopping execution.")
        print("Final output:", enforcer.output)
        break

    if a not in A_and.S:
        print("Invalid symbol!")
        continue

    released = enforcer.step(a)
    tentative, committed = enforcer.debug_state()

    print(f"  Buffer σc           : {enforcer.sigma_c}")
    print(f"  state               : {tentative}")
    print(f"  Final Output so far : {released} \n")
