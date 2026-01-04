#!/usr/bin/env python3
"""
Performance Evaluation
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

# Import DFA definitions 

from helper.dfa_definitions import (
    get_all_Strict_mono_dfas,
    get_all_Strict_serial_dfas,
    get_all_Strict_parallel_dfas,
    get_all_LE_mono_dfas,
    get_all_LE_parallel_dfas,
)

from helper.exclusive_modified_automata import get_all_exclusive_modified

# Import Enforcers

from Source.least_effort_mono import least_effort_monolithic_enforcer
from Source.least_effort_parallel import LeastEffortParallelEnforcer

from Source.strict_mono import StrictMonolithicEnforcer
from Source.strict_serial import StrictSerialEnforcer
from Source.strict_parallel import StrictParallelEnforcer

from Source.exclusive_mono import ExclusiveMonolithicEnforcer
from Source.exclusive_parallel import ExclusiveParallelEnforcer

from helper.product import product

# Load DFAs

strict_mono_dfas     = get_all_Strict_mono_dfas()
strict_serial_dfas   = get_all_Strict_serial_dfas()
strict_parallel_dfas = get_all_Strict_parallel_dfas()

le_mono_dfas     = get_all_LE_mono_dfas()
le_parallel_dfas = get_all_LE_parallel_dfas()

exclusive_modified_dfas = get_all_exclusive_modified()

# -------------------------------------------------
# Enforcer configurations
# -------------------------------------------------

enforcers = {
    "LE_Monolithic": {
        "factory": lambda: least_effort_monolithic_enforcer("LE", *le_mono_dfas),
        "alphabet": list(le_mono_dfas[0].S),
        "type": "LE_monolithic",
    },
    "LE_Parallel": {
        "factory": lambda: LeastEffortParallelEnforcer(le_parallel_dfas),
        "alphabet": list(le_parallel_dfas[0].S),
        "type": "LE_parallel",
    },
    "Strict_Monolithic": {
        "factory": lambda: None,   # handled inside timer
        "alphabet": list(strict_mono_dfas[0].S),
        "type": "strict_monolithic",
    },
    "Strict_Serial": {
        "factory": lambda: StrictSerialEnforcer(strict_serial_dfas),
        "alphabet": list(strict_serial_dfas[0].S),
        "type": "strict_serial",
    },
    "Strict_Parallel": {
        "factory": lambda: StrictParallelEnforcer(strict_parallel_dfas),
        "alphabet": list(strict_parallel_dfas[0].S),
        "type": "strict_parallel",
    },
    "Exclusive_Monolithic": {
        "factory": lambda: None,   # handled inside timer
        "alphabet": list(exclusive_modified_dfas[0].S),
        "type": "exclusive_monolithic",
    },
    "Exclusive_Parallel": {
        "factory": lambda: ExclusiveParallelEnforcer(exclusive_modified_dfas),
        "alphabet": list(exclusive_modified_dfas[0].S),
        "type": "exclusive_parallel",
    },
}

INPUT_SIZES = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# Helpers

def generate_input(alphabet, n):
    return [random.choice(alphabet) for _ in range(n)]


def time_enforcer(enf, enf_type, input_list):

    if enf_type == "LE_monolithic":
        t0 = time.time()
        for a in input_list:
            enf(a)
        return time.time() - t0

    elif enf_type == "LE_parallel":
        t0 = time.time()
        for a in input_list:
            enf.process_event(a)
        return time.time() - t0

    elif enf_type == "strict_parallel":
        t0 = time.time()
        for a in input_list:
            enf.step(a)
        return time.time() - t0

    elif enf_type == "strict_serial":
        t0 = time.time()
        for a in input_list:
            enf.step(a)
        return time.time() - t0

    elif enf_type == "strict_monolithic":
        enf = StrictMonolithicEnforcer(strict_mono_dfas)
        
        t0 = time.time()
        for a in input_list:
            enf.step(a)
        return time.time() - t0

    elif enf_type == "exclusive_monolithic":
        t_prod_start = time.time()
        mono_dfa = product(*exclusive_modified_dfas, "Exclusive_Mono")
        mono_enf = ExclusiveMonolithicEnforcer(mono_dfa)
        t_prod = time.time() - t_prod_start

        t_run_start = time.time()
        for a in input_list:
            mono_enf.step(a)
        t_run = time.time() - t_run_start

        return t_prod + t_run

    elif enf_type == "exclusive_parallel":
        t0 = time.time()
        for a in input_list:
            enf.step(a)
        return time.time() - t0


# -------------------------------------------------
# Run evaluation
# -------------------------------------------------

results = []

for name, cfg in enforcers.items():
    print(f"\n----- {name} -----")
    for n in INPUT_SIZES:
        enf = cfg["factory"]()
        seq = generate_input(cfg["alphabet"], n)
        total = time_enforcer(enf, cfg["type"], seq)
        print(f"{name} | {n} events | {total:.6f} sec")
        results.append([name, n, total])

# -------------------------------------------------
# Save CSV
# -------------------------------------------------

with open("performance_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Enforcer", "Input Size", "Total Time (s)"])
    writer.writerows(results)

print("\nSaved performance_results.csv")
