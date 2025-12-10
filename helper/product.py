#!/usr/bin/env python3
"""
helper_products.py

"""

import sys
sys.path.append("..")

import helper.Automata as Automata
from helper.Automata import DFA as BaseDFA


# Helper state class
class state(object):
    def __init__(self, name):
        self.name = name
        self.transit = dict()


class DFA(BaseDFA):
    """
    Extended DFA class used for compositional enforcement.

    Attributes:
        name   : Name of the automaton
        end    : List of accepting states (explicit representation)
        buffer : Temporary buffer (used only in bounded enforcer contexts)
    """

    def __init__(self, name, S, Q, q0, F, d, end, e=('.l',)):
        super().__init__(S, Q, q0, F, d, e)
        self.name = name
        self.end = end
        self.buffer = []


    # ----------------State Transition Helpers----------------- 

    def is_safe(self, current_state, event_sequence):
        """
        Checking if applying event_sequence from current_state reaches an accepting state.
        """
        state = current_state
        for e in event_sequence:
            state = self.d(state, e)
            if state is None:
                return False
        return state in self.end

    def next_state(self, current_state, event_sequence):
        """
        Return the state reached after consuming event_sequence from current_state.
        """
        state = current_state
        for e in event_sequence:
            state = self.d(state, e)
            if state is None:
                break
        return state


################## OR/AND-Product DFAs ########################

def product_and(A, B, p_name):
    """
    AND-product DFA.
    Accepting condition: both A and B accept.
    """

    assert A.S == B.S, "Alphabets must match!"

    p_states = [f"{qA}_{qB}" for qA in A.Q for qB in B.Q]
    p_start = f"{A.q0}_{B.q0}"

    def p_F(p_state):
        qA, qB = p_state.split("_", 1)
        return A.F(qA) and B.F(qB)

    p_end = [s for s in p_states if p_F(s)]

    def p_d(p_state, symbol):
        qA, qB = p_state.split("_", 1)
        nextA = A.d(qA, symbol)
        nextB = B.d(qB, symbol)
        if nextA is None or nextB is None:
            return None
        return f"{nextA}_{nextB}"

    return DFA(p_name, A.S, p_states, p_start, p_F, p_d, p_end)

product = product_and


def product_or(A, B, p_name):
    """
    OR-product DFA.

    Accepting condition: at least one DFA accepts.
    States are encoded as "qA_qB".

    """

    assert A.S == B.S, "Alphabets must match!"

    p_states = [f"{qA}_{qB}" for qA in A.Q for qB in B.Q]
    p_start = f"{A.q0}_{B.q0}"

    def p_F(p_state):
        qA, qB = p_state.split("_", 1)
        return A.F(qA) or B.F(qB)

    p_end = [s for s in p_states if p_F(s)]

    def p_d(p_state, symbol):
        qA, qB = p_state.split("_", 1)
        nextA = A.d(qA, symbol)
        nextB = B.d(qB, symbol)
        if nextA is None or nextB is None:
            return None
        return f"{nextA}_{nextB}"

    return DFA(p_name, A.S, p_states, p_start, p_F, p_d, p_end)
