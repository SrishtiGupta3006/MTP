#!/usr/bin/env python3
"""
output_strict_parallel.py
Runtime simulation for Strict Parallel Enforcer (Algorithm 3)
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Source.strict_parallel import StrictParallelEnforcer
from helper.product import DFA

# -------------------------------------------------
# Define DFAs (phi1, phi2)
# -------------------------------------------------

states = ['stop', 'start', 'right', 'left', 'forward', 'back']

transition_dict = {
    ('start','r'):'right', ('start','l'):'left', ('start','f'):'forward', ('start','b'):'back', ('start','s'):'stop',
    ('right','r'):'right', ('right','l'):'left', ('right','f'):'forward', ('right','b'):'back', ('right','s'):'stop',
    ('left','r'):'right', ('left','l'):'left', ('left','f'):'forward', ('left','b'):'back', ('left','s'):'stop',
    ('forward','r'):'right', ('forward','l'):'left', ('forward','f'):'forward', ('forward','b'):'back', ('forward','s'):'stop',
    ('back','r'):'right', ('back','l'):'left', ('back','f'):'forward', ('back','b'):'back', ('back','s'):'stop',
    ('stop','r'):'stop', ('stop','l'):'stop', ('stop','f'):'stop', ('stop','b'):'stop', ('stop','s'):'stop',
}

phi1 = DFA(
    "phi1",
    ['r','l','f','b','s'],
    states,
    'start',
    lambda q: q == 'right',
    lambda q,a: transition_dict[(q,a)],
    ['right']
)

phi2 = DFA(
    "phi2",
    ['r','l','f','b','s'],
    states,
    'start',
    lambda q: q == 'left',
    lambda q,a: transition_dict[(q,a)],
    ['left']
)

# -------------------------------------------------
# Strict Parallel Enforcer
# -------------------------------------------------

enforcer = StrictParallelEnforcer([phi1, phi2])

print("\n=== Strict Parallel Enforcer ===")
print("Valid inputs: r, l, f, b, s")
print("Type 'end' to stop\n")

while True:
    a = input("Input event: ").strip()

    if a == "end":
        print("\nStopping execution.")
        break

    if a not in ['r','l','f','b','s']:
        print("Invalid input.")
        continue

    released = enforcer.step(a)

    print("Released output :", released)
    print("Current states  :", enforcer.q)
    print("Global output   :", enforcer.output)
    print("-" * 50)
