#!/usr/bin/env python3
"""
Property-Scaling Performance Evaluation

Measures scalability by increasing number of properties
while keeping input length fixed.

Enforcers evaluated:
- Least Effort Parallel
- Strict Parallel
- Exclusive Parallel
"""

import time
import csv
import random
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from helper.product import DFA as ProductDFA
from Source.least_effort_parallel import LeastEffortParallelEnforcer
from Source.strict_parallel import StrictParallelEnforcer
from Source.exclusive_parallel import ExclusiveParallelEnforcer
from Source.exclusive_modified_automata import get_all_exclusive_modified


# -------------------------------------------------------
# Base DFA for LE & Strict
# -------------------------------------------------------

states = ['stop', 'start', 'right', 'left', 'forward', 'back']

transition_dict = {
    ('start','r'):'right', ('start','l'):'left', ('start','f'):'forward',
    ('start','b'):'back', ('start','s'):'stop',
    ('right','r'):'right', ('right','l'):'left', ('right','f'):'forward',
    ('right','b'):'back', ('right','s'):'stop',
    ('left','r'):'right', ('left','l'):'left', ('left','f'):'forward',
    ('left','b'):'back', ('left','s'):'stop',
    ('forward','r'):'right', ('forward','l'):'left', ('forward','f'):'forward',
    ('forward','b'):'back', ('forward','s'):'stop',
    ('back','r'):'right', ('back','l'):'left', ('back','f'):'forward',
    ('back','b'):'back', ('back','s'):'stop',
    ('stop','r'):'stop', ('stop','l'):'stop', ('stop','f'):'stop',
    ('stop','b'):'stop', ('stop','s'):'stop',
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
# Parameters
# -------------------------------------------------------

PROPERTY_COUNTS = [1, 2, 4, 8]
FIXED_INPUT_SIZE = 5000

# -------------------------------------------------------
# Inputs
# -------------------------------------------------------

def generate_input(alphabet, n):
    return [random.choice(alphabet) for _ in range(n)]

input_standard = generate_input(base_phi.S, FIXED_INPUT_SIZE)

# -------------------------------------------------------
# Exclusive DFAs (modified)
# -------------------------------------------------------

exclusive_dfas_all = get_all_exclusive_modified()
exclusive_alphabet = list(exclusive_dfas_all[0].S)

input_exclusive = generate_input(exclusive_alphabet, FIXED_INPUT_SIZE)

# -------------------------------------------------------
# Run evaluation
# -------------------------------------------------------

results = []

for k in PROPERTY_COUNTS:
    print(f"\n=== Properties: {k} ===")

    # -------- Least Effort Parallel --------
    le_props = [base_phi for _ in range(k)]
    le_enf = LeastEffortParallelEnforcer(le_props)

    t0 = time.time()
    for a in input_standard:
        le_enf.process_event(a)
    total = time.time() - t0
    print(f"LE_Parallel | {k} | {total:.6f}")
    results.append(["LE_Parallel", k, total])

    # -------- Strict Parallel --------
    sp_props = [base_phi for _ in range(k)]
    sp_enf = StrictParallelEnforcer(sp_props)

    t0 = time.time()
    for a in input_standard:
        sp_enf.step(a)
    total = time.time() - t0
    print(f"Strict_Parallel | {k} | {total:.6f}")
    results.append(["Strict_Parallel", k, total])

    # -------- Exclusive Parallel --------
    ex_props = exclusive_dfas_all[:k]
    ex_enf = ExclusiveParallelEnforcer(ex_props)

    t0 = time.time()
    for a in input_exclusive:
        ex_enf.step(a)
    total = time.time() - t0
    print(f"Exclusive_Parallel | {k} | {total:.6f}")
    results.append(["Exclusive_Parallel", k, total])

# -------------------------------------------------------
# Save CSV
# -------------------------------------------------------

with open("performance_properties_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Enforcer", "Num_Properties", "Total_Time(s)"])
    writer.writerows(results)

print("\nSaved performance_properties_results.csv")
