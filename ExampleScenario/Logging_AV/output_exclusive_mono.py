#!/usr/bin/env python3

import sys
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)
sys.path.append(PROJECT_ROOT)

from helper.product import product
from Source.exclusive_modified_automata import A1_mod, A2_mod
from Source.exclusive_mono import ExclusiveMonolithicEnforcer

# Build Exclusive Monolithic Enforcer

A_and = product(A1_mod, A2_mod, "Exclusive_Mono")
enforcer = ExclusiveMonolithicEnforcer(A_and)

print("\n=== Exclusive Monolithic Enforcer (Algorithm 6) ===")
print("Valid inputs: [ f, l, o, n ]")
print("Type 'end' to stop\n")

# Interactive loop

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
