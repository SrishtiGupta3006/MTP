#!/usr/bin/env python3
"""
output_exclusive_parallel.py
"""

import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from Source.exclusive_parallel_1_opt import ExclusiveParallelEnforcer
from helper.exclusive_modified_automata import get_all_exclusive_modified


# get ALL modified DFAs A′₁, …, A′ₙ
modified_dfas = get_all_exclusive_modified()

# Exclusive Parallel Enforcer over modified DFAs
enf = ExclusiveParallelEnforcer(modified_dfas)

print("Interactive Exclusive Parallel Enforcer")
print("Enter events one by one (valid: f, o, l, n, r). Type 'end' to stop.\n")

final_output = ""

while True:
    a = input("Enter event: ").strip()

    if a.lower() in ["end", "quit", "q"]:
        print("Stopping...")
        break

    if a not in modified_dfas[0].S:
        print("Invalid event!")
        continue

    out, debug = enf.step(a)

    for info in debug:
        print(
            f"Enforcer {info['enforcer']} → "
            f"state = {info['state']}, "
            f"σc = {info['σc']}, "
            f"σs = {info['σs']}"
        )

    emitted_string = ''.join(out)
    final_output += emitted_string

    if emitted_string:
        print(f"Emitted Output: {out}  -> string: '{emitted_string}'")

    print(f"Final Output so far: '{final_output}'\n")
