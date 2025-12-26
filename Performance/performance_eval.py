#!/usr/bin/env python3
"""
Scalability Performance Evaluation

Evaluates total execution time for:
- Least Effort Monolithic
- Least Effort Parallel
- Strict Monolithic
- Strict Serial
- Exclusive Monolithic (Algorithm 6)
- Exclusive Parallel

Input sizes:
100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000
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
from helper.product import product

from Source.least_effort_mono import least_effort_monolithic_enforcer
from Source.least_effort_parallel import LeastEffortParallelEnforcer

from Source.strict_mono import monolithic_enforcer
from Source.strict_serial import serial_enforcer
from Source.strict_parallel import StrictParallelEnforcer

from helper.exclusive_modified_automata import get_all_exclusive_modified
from Source.exclusive_mono import ExclusiveMonolithicEnforcer
from Source.exclusive_parallel import ExclusiveParallelEnforcer

# Get all modified DFAs A′₁ … A′ₙ
exclusive_modified_dfas = get_all_exclusive_modified()

# Define phi1 and phi2 (used for LE & Strict)

states = ['stop', 'start', 'right', 'left', 'forward', 'back']

transition_dict = {
    ('start','r'):'right', ('start','l'):'left', ('start','f'):'forward', ('start','b'):'back', ('start','s'):'stop',
    ('right','r'):'right', ('right','l'):'left', ('right','f'):'forward', ('right','b'):'back', ('right','s'):'stop',
    ('left','r'):'right', ('left','l'):'left', ('left','f'):'forward', ('left','b'):'back', ('left','s'):'stop',
    ('forward','r'):'right', ('forward','l'):'left', ('forward','f'):'forward', ('forward','b'):'back', ('forward','s'):'stop',
    ('back','r'):'right', ('back','l'):'left', ('back','f'):'forward', ('back','b'):'back', ('back','s'):'stop',
    ('stop','r'):'stop', ('stop','l'):'stop', ('stop','f'):'stop', ('stop','b'):'stop', ('stop','s'):'stop',
}

phi1 = ProductDFA(
    "phi1",
    ['r','l','f','b','s'],
    states,
    'start',
    lambda q: q == 'right',
    lambda q,a: transition_dict[(q,a)],
    ['right']
)

phi2 = ProductDFA(
    "phi2",
    ['r','l','f','b','s'],
    states,
    'start',
    lambda q: q == 'left',
    lambda q,a: transition_dict[(q,a)],
    ['left']
)

# Exclusive Monolithic DFA (A′₁ ⊗ A′₂)

exclusive_mono_dfa = product(*exclusive_modified_dfas, "Exclusive_Mono")

# Enforcer

enforcers = {
    "LE_Monolithic": {
        "factory": lambda: least_effort_monolithic_enforcer("LE", phi1, phi2),
        "alphabet": ['r','l','f','b','s'],
        "type": "streaming"
    },
    "LE_Parallel": {
        "factory": lambda: LeastEffortParallelEnforcer([phi1, phi2]),
        "alphabet": ['r','l','f','b','s'],
        "type": "parallel"
    },
    "Strict_Monolithic": {
        "factory": lambda: monolithic_enforcer("SM", phi1, phi2),
        "alphabet": ['r','l','f','b','s'],
        "type": "dfa_product"
    },
    "Strict_Serial": {
        "factory": lambda: serial_enforcer("SS", phi1, phi2),
        "alphabet": ['r','l','f','b','s'],
        "type": "serial"
    },
    "Strict_Parallel": {
        "factory": lambda: StrictParallelEnforcer([phi1, phi2]),
        "alphabet": ['r','l','f','b','s'],
        "type": "strict_parallel"
    },
    "Exclusive_Monolithic": {
        "factory": lambda: ExclusiveMonolithicEnforcer(exclusive_mono_dfa),
        "alphabet": list(exclusive_modified_dfas[0].S),
        "type": "exclusive_monolithic"
    },
    "Exclusive_Parallel": {
        "factory": lambda: ExclusiveParallelEnforcer(exclusive_modified_dfas),
        "alphabet": list(exclusive_modified_dfas[0].S),
        "type": "exclusive_parallel"
    }
}

# Input sizes

INPUT_SIZES = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# Helpers

def generate_input(alphabet, n):
    return [random.choice(alphabet) for _ in range(n)]

def time_enforcer(enf, enf_type, input_list):
    t0 = time.time()

    if enf_type == "streaming":
        for a in input_list:
            enf(a)

    elif enf_type == "parallel":
        for a in input_list:
            enf.process_event(a)
    
    elif enf_type == "strict_parallel":
        for a in input_list:
            enf.step(a)

    elif enf_type == "serial":
        with contextlib.redirect_stdout(io.StringIO()):
            enf(input_list)

    elif enf_type == "dfa_product":
        q = enf.q0
        for a in input_list:
            q = enf.d(q, a)

    elif enf_type == "exclusive_monolithic":
        for a in input_list:
            enf.step(a)

    elif enf_type == "exclusive_parallel":
        for a in input_list:
            enf.step(a)

    return time.time() - t0

# Running evaluation

results = []

for name, cfg in enforcers.items():
    print(f"\n----- {name} -----")

    for n in INPUT_SIZES:
        enf = cfg["factory"]()          # 🔑 fresh instance every time
        seq = generate_input(cfg["alphabet"], n)

        total = time_enforcer(enf, cfg["type"], seq)

        print(f"{name} | {n} events | {total:.6f} sec")
        results.append([name, n, total])

# Save CSV

with open("performance_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Enforcer", "Input Size", "Total Time (s)"])
    writer.writerows(results)

print("\nSaved performance_results.csv")