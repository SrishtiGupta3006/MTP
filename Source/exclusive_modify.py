# Source/exclusive_modify.py

from helper.Automata import DFA


def modify_for_exclusive_n(orig_dfa, own_deciding, others_deciding):
    """
    n-ary exclusive modification for a single DFA.
    Assumes deciding event sets are pairwise disjoint.
    """

    Q_new = list(orig_dfa.Q)
    qX_map = {}

    prefix = orig_dfa.Q[0][0]
    next_index = len(orig_dfa.Q)

    for q in orig_dfa.Q:
        qX = f"{prefix}{next_index}"
        qX_map[q] = qX
        Q_new.append(qX)
        next_index += 1

    F_new = lambda q: orig_dfa.F(q) or q in qX_map.values()
    d_orig = orig_dfa.d

    def d_new(q, a):
        if q in qX_map.values():
            orig = next(k for k, v in qX_map.items() if v == q)
            return d_orig(orig, a) if a in own_deciding else q
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
