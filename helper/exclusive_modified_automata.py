# Source/exclusive_modified_automata.py

from helper.Automata import DFA
from helper.dfa_definitions import get_all_dfas


# =====================================================
# Exclusive DFA modification (n-ary)
# =====================================================

def modify_for_exclusive(orig_dfa, own_deciding, others_deciding):
    """
    n-ary exclusive modification for a single DFA.

    - own_deciding: events on which this DFA resumes
    - others_deciding: events that block this DFA

    Assumes deciding event sets are pairwise disjoint.
    """

    Q_new = list(orig_dfa.Q)
    qX_map = {}   # original state -> don't-care state

    prefix = orig_dfa.Q[0][0]
    next_index = len(orig_dfa.Q)

    # Create don't-care states
    for q in orig_dfa.Q:
        qX = f"{prefix}{next_index}"
        qX_map[q] = qX
        Q_new.append(qX)
        next_index += 1

    # Accepting states: original accepting OR don't-care
    F_new = lambda q: orig_dfa.F(q) or q in qX_map.values()
    d_orig = orig_dfa.d

    # Modified transition function
    def d_new(q, a):
        # If already blocked (don't-care)
        if q in qX_map.values():
            orig = next(k for k, v in qX_map.items() if v == q)
            return d_orig(orig, a) if a in own_deciding else q

        # Normal state
        else:
            return qX_map[q] if a in others_deciding else d_orig(q, a)

    return DFA(
        S=orig_dfa.S,
        Q=Q_new,
        q0=orig_dfa.q0,
        F=F_new,
        d=d_new,
        e=orig_dfa.e
    )


# =====================================================
# Builder: all exclusive-modified DFAs
# =====================================================

def get_all_exclusive_modified():
    """
    Returns exclusive-modified DFAs A′₁ … A′ₙ
    constructed from the canonical DFA definitions.
    """

    dfas_with_deciding = get_all_dfas()
    modified = []

    for i, (dfa, own_deciding) in enumerate(dfas_with_deciding):
        others_deciding = set().union(
            *[ev for j, (_, ev) in enumerate(dfas_with_deciding) if j != i]
        )

        modified.append(
            modify_for_exclusive(dfa, own_deciding, others_deciding)
        )

    return modified
