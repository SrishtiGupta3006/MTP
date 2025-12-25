#!/usr/bin/env python3
"""
Property-Scaling Performance Evaluation

Measures scalability by increasing number of properties
while keeping input length fixed.

Enforcers evaluated:
- Least Effort Parallel
- Strict Parallel
- Exclusive Parallel

Input length: fixed
Metric: total execution time
"""

import time
import csv
import random
import sys
import os
import contextlib
import io

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from helper.product import DFA as ProductDFA
from Source.least_effort_parallel import LeastEffortParallelEnforcer
from Source.strict_parallel import StrictParallelEnforcer
from Source.exclusive_parallel import ExclusiveParallelEnforcer
from Source.exclusive_modified_automata import A1_mod

# -------------------------------------------------------
# Base DFA 

states = ['stop', 'start', 'right', 'left', 'forward', 'back']

transition_dict = {
    ('start','r'):'right', ('start','l'):'left', ('start','f'):'forward', ('start','b'):'back', ('start','s'):'stop',
    ('right','r'):'right', ('right','l'):'left', ('right','f'):'forward', ('right','b'):'back', ('right','s'):'stop',
    ('left','r'):'right', ('left','l'):'left', ('left','f'):'forward', ('left','b'):'back', ('left','s'):'stop',
    ('forward','r'):'right', ('forward','l'):'left', ('forward','f'):'forward', ('forward','b'):'back', ('forward','s'):'stop',
    ('back','r'):'right', ('back','l'):'left', ('back','f'):'forward', ('back','b'):'back', ('back','s'):'stop',
    ('stop','r'):'stop', ('stop','l'):'stop', ('stop','f'):'stop', ('stop','b'):'stop', ('stop','s'):'stop',
}

base_phi = ProductDFA(
    "phi",
    ['r','l','f','b','s'],
    states,
    'start',
    lambda q: q == 'right',
    lambda q,a: transition_dict[(q,a)],
    ['right']
)

# -------------------------------------------------------
# parameters

PROPERTY_COUNTS = [1, 2, 4, 8, 16, 32]
FIXED_INPUT_SIZE = 5000

ALPHABET_STANDARD = ['r','l','f','b','s']
ALPHABET_EXCLUSIVE = ['f','l','o','n']

# -------------------------------------------------------
# Helpers


def generate_input(alphabet, n):
    return [random.choice(alphabet) for _ in range(n)]

def duplicate_properties(prop, k):
    return [prop for _ in range(k)]

# -------------------------------------------------------
# Run evaluation
# -------------------------------------------------------

results = []

input_standard = generate_input(ALPHABET_STANDARD, FIXED_INPUT_SIZE)
input_exclusive = generate_input(ALPHABET_EXCLUSIVE, FIXED_INPUT_SIZE)

for k in PROPERTY_COUNTS:
    print(f"\n=== Properties: {k} ===")

    # -------- Least Effort Parallel --------
    le_props = duplicate_properties(base_phi, k)
    le_enf = LeastEffortParallelEnforcer(le_props)

    t0 = time.time()
    for a in input_standard:
        le_enf.process_event(a)
    total = time.time() - t0

    print(f"LE_Parallel | {k} properties | {total:.6f} sec")
    results.append(["LE_Parallel", k, total])

    # -------- Strict Parallel --------
    sp_props = duplicate_properties(base_phi, k)
    sp_enf = StrictParallelEnforcer(sp_props)

    t0 = time.time()
    for a in input_standard:
        sp_enf.step(a)
    total = time.time() - t0

    print(f"Strict_Parallel | {k} properties | {total:.6f} sec")
    results.append(["Strict_Parallel", k, total])

    # -------- Exclusive Parallel --------
    ex_props = [A1_mod for _ in range(k)]
    ex_enf = ExclusiveParallelEnforcer(ex_props)

    t0 = time.time()
    for a in input_exclusive:
        ex_enf.step(a)
    total = time.time() - t0

    print(f"Exclusive_Parallel | {k} properties | {total:.6f} sec")
    results.append(["Exclusive_Parallel", k, total])

# -------------------------------------------------------
# Save CSV

with open("performance_properties_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Enforcer", "Num_Properties", "Total_Time(s)"])
    writer.writerows(results)

print("\nSaved performance_properties_results.csv")
