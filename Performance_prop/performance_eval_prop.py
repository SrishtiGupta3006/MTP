#!/usr/bin/env python3
"""
Performance Evaluation w.r.t Number of Properties
"""

import time
import csv
import random
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

# Imports

from Performance_prop.dfa_definitions_prop import (
    get_all_Strict_mono_dfas,
    get_all_Strict_serial_dfas,
    get_all_Strict_parallel_dfas,
    get_all_LE_mono_dfas,
    get_all_LE_parallel_dfas,
)

from helper.exclusive_modified_automata import get_all_exclusive_modified
from helper.product import product

from Source.least_effort_mono import least_effort_monolithic_enforcer
from Source.least_effort_parallel import LeastEffortParallelEnforcer

from Source.strict_mono import StrictMonolithicEnforcer
from Source.strict_serial import StrictSerialEnforcer
from Source.strict_parallel import StrictParallelEnforcer

from Source.exclusive_mono import ExclusiveMonolithicEnforcer
from Source.exclusive_parallel import ExclusiveParallelEnforcer

# -------------------------------------------------
# Load ALL DFAs
# -------------------------------------------------

STRICT_MONO_ALL     = get_all_Strict_mono_dfas()
STRICT_SERIAL_ALL   = get_all_Strict_serial_dfas()
STRICT_PARALLEL_ALL = get_all_Strict_parallel_dfas()

LE_MONO_ALL         = get_all_LE_mono_dfas()
LE_PARALLEL_ALL     = get_all_LE_parallel_dfas()

EXCLUSIVE_ALL       = get_all_exclusive_modified()

# -------------------------------------------------
# Experiment parameters
# -------------------------------------------------

INPUT_SIZE = 100

MAX_PROPS = {
    "Strict_Monolithic": 10,
    "Strict_Serial": 14,
    "Strict_Parallel": 14,
    "LE_Monolithic": 6,
    "LE_Parallel": 6,
    "Exclusive_Monolithic": 10,
    "Exclusive_Parallel": 14,
}

# -------------------------------------------------
# Helpers
# -------------------------------------------------

def generate_input(alphabet, n):
    return [random.choice(alphabet) for _ in range(n)]


def time_enforcer(enf, enf_type, input_list):
    t0 = time.perf_counter()

    if enf_type in {
        "strict_monolithic",
        "strict_serial",
        "strict_parallel",
        "exclusive_monolithic",
        "exclusive_parallel",
    }:
        for a in input_list:
            enf.step(a)

    elif enf_type == "LE_monolithic":
        for a in input_list:
            enf(a)

    elif enf_type == "LE_parallel":
        for a in input_list:
            enf.process_event(a)

    return (time.perf_counter() - t0) * 1_000_000  # microseconds

# -------------------------------------------------
# Run evaluation
# -------------------------------------------------

results = []

ENFORCER_ORDER = [
    "Strict_Monolithic",
    "Strict_Serial",
    "Strict_Parallel",
    "LE_Monolithic",
    "LE_Parallel",
    "Exclusive_Monolithic",
    "Exclusive_Parallel",
]

for name in ENFORCER_ORDER:
    print(f"\n----- {name} -----")

    property_range = range(2, MAX_PROPS[name] + 1)

    for k in property_range:

        # Slice DFAs
        strict_mono_dfas     = STRICT_MONO_ALL[:k]
        strict_serial_dfas   = STRICT_SERIAL_ALL[:k]
        strict_parallel_dfas = STRICT_PARALLEL_ALL[:k]

        le_mono_dfas         = LE_MONO_ALL[:k]
        le_parallel_dfas     = LE_PARALLEL_ALL[:k]

        exclusive_dfas       = EXCLUSIVE_ALL[:k]

        # Build enforcer
        try:
            if name == "Strict_Monolithic":
                enf = StrictMonolithicEnforcer(strict_mono_dfas)
                alphabet = list(strict_mono_dfas[0].S)
                enf_type = "strict_monolithic"

            elif name == "Strict_Serial":
                enf = StrictSerialEnforcer(strict_serial_dfas)
                alphabet = list(strict_serial_dfas[0].S)
                enf_type = "strict_serial"

            elif name == "Strict_Parallel":
                enf = StrictParallelEnforcer(strict_parallel_dfas)
                alphabet = list(strict_parallel_dfas[0].S)
                enf_type = "strict_parallel"

            elif name == "LE_Monolithic":
                enf = least_effort_monolithic_enforcer("LE", *le_mono_dfas)
                alphabet = list(le_mono_dfas[0].S)
                enf_type = "LE_monolithic"

            elif name == "LE_Parallel":
                enf = LeastEffortParallelEnforcer(le_parallel_dfas)
                alphabet = list(le_parallel_dfas[0].S)
                enf_type = "LE_parallel"

            elif name == "Exclusive_Monolithic":
                exclusive_mono_dfa = product(*exclusive_dfas, "Exclusive_Mono")
                enf = ExclusiveMonolithicEnforcer(exclusive_mono_dfa)
                alphabet = list(exclusive_dfas[0].S)
                enf_type = "exclusive_monolithic"

            elif name == "Exclusive_Parallel":
                enf = ExclusiveParallelEnforcer(exclusive_dfas)
                alphabet = list(exclusive_dfas[0].S)
                enf_type = "exclusive_parallel"

        except MemoryError:
            print(f"{name} | {k} properties | MEMORY ERROR (state explosion)")
            continue

        # Run experiment
        seq = generate_input(alphabet, INPUT_SIZE)
        total = time_enforcer(enf, enf_type, seq)

        print(f"{name} | {k} properties | {total:.2f} µs")
        results.append([name, k, INPUT_SIZE, total])

# Save CSV

with open("performance_properties.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Enforcer",
        "Num_Properties",
        "Input_Size",
        "Total_Time (microseconds)"
    ])
    writer.writerows(results)

print("\nSaved performance_properties.csv")
