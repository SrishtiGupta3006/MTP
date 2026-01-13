#!/usr/bin/env python3
"""
product.py
Generalised n-ary DFA product construction
"""

import sys

sys.path.append("..")

from itertools import product as cartesian_product
import helper.Automata as Automata
from helper.Automata import DFA as BaseDFA


# Helper State Class

class state(object):
    def __init__(self, name):
        self.name = name
        self.transit = dict()


# DFA 

class DFA(BaseDFA):
    """
    Extended DFA class used for compositional enforcement.
    """

    def __init__(self, name, S, Q, q0, F, d, end, e=('.l',)):
        super().__init__(S, Q, q0, F, d, e)
        self.name = name
        self.end = end
        self.buffer = []

    def is_safe(self, current_state, event_sequence):
        state = current_state
        for e in event_sequence:
            state = self.d(state, e)
            if state is None:
                return False
        return state in self.end

    def next_state(self, current_state, event_sequence):
        state = current_state
        for e in event_sequence:
            state = self.d(state, e)
            if state is None:
                break
        return state


# ================= AND Product ================= #

def product_and(*args):
    """
    n-ary AND-product DFA.
    Accepting condition: ALL DFAs accept.

    Usage:
        product_and(A, B, name)
        product_and(A1, A2, A3, ..., name)
    """

    assert len(args) >= 3, "Provide at least two DFAs and a product name"

    *automata, p_name = args
    assert len(automata) >= 2, "At least two DFAs are required"

    # Alphabet consistency
    S = automata[0].S
    for A in automata:
        assert A.S == S, "Alphabets must match!"

    # Product states
    p_states = [
        "_".join(states)
        for states in cartesian_product(*[A.Q for A in automata])
    ]

    # Initial state
    p_start = "_".join([A.q0 for A in automata])

    # Accepting condition
    def p_F(p_state):
        states = p_state.split("_")
        return all(A.F(q) for A, q in zip(automata, states))

    p_end = [s for s in p_states if p_F(s)]

    # Transition function
    def p_d(p_state, symbol):
        states = p_state.split("_")
        next_states = []

        for A, q in zip(automata, states):
            nq = A.d(q, symbol)
            if nq is None:
                return None
            next_states.append(nq)

        return "_".join(next_states)

    assert p_start in p_states
    assert len(p_states) > 0

    return DFA(p_name, S, p_states, p_start, p_F, p_d, p_end)


# ================= OR Product ================= #

def product_or(*args):
    """
    n-ary OR-product DFA.
    Accepting condition: AT LEAST ONE DFA accepts.
    """

    assert len(args) >= 3, "Provide at least two DFAs and a product name"

    *automata, p_name = args
    assert len(automata) >= 2, "At least two DFAs are required"

    S = automata[0].S
    for A in automata:
        assert A.S == S, "Alphabets must match!"

    p_states = [
        "_".join(states)
        for states in cartesian_product(*[A.Q for A in automata])
    ]

    p_start = "_".join([A.q0 for A in automata])

    def p_F(p_state):
        states = p_state.split("_")
        return any(A.F(q) for A, q in zip(automata, states))

    p_end = [s for s in p_states if p_F(s)]

    def p_d(p_state, symbol):
        states = p_state.split("_")
        next_states = []

        for A, q in zip(automata, states):
            nq = A.d(q, symbol)
            if nq is None:
                return None
            next_states.append(nq)

        return "_".join(next_states)

    assert p_start in p_states
    assert len(p_states) > 0

    return DFA(p_name, S, p_states, p_start, p_F, p_d, p_end)

# Backward compatibility alias
product = product_and
