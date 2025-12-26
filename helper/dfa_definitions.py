# dfa_definitions.py

from helper.Automata import DFA

# A1 : decides on 'l'
def exclusive_phi1():
    def d1(q, a):
        transitions = {
            "q0": {"f": "q1", "l": "q0", "o": "q0", "n": "q0", "r": "q0"},
            "q1": {"l": "q2", "f": "q1", "o": "q1", "n": "q1", "r": "q1"},
            "q2": {"f": "q1", "l": "q2", "o": "q2", "n": "q2", "r": "q2"},
        }
        return transitions[q].get(a, q)

    A1 = DFA(
        S={"f", "l", "o", "n", "r"},
        Q=["q0", "q1", "q2"],
        q0="q0",
        F=lambda q: q == "q2",
        d=d1
    )
    A1.name = "A1"

    return A1, {"l"}


# A2 : decides on 'n'
def exclusive_phi2():
    def d2(q, a):
        transitions = {
            "p0": {"o": "p1", "f": "p0", "l": "p0", "n": "p0", "r": "p0"},
            "p1": {"n": "p2", "f": "p1", "l": "p1", "o": "p1", "r": "p1"},
            "p2": {"f": "p2", "l": "p2", "o": "p2", "n": "p2", "r": "p2"},
        }
        return transitions[q].get(a, q)

    A2 = DFA(
        S={"f", "l", "o", "n", "r"},
        Q=["p0", "p1", "p2"],
        q0="p0",
        F=lambda q: q == "p2",
        d=d2
    )
    A2.name = "A2"

    return A2, {"n"}


def get_all_dfas():
    """
    Add/remove DFAs ONLY here.
    """
    return [
        exclusive_phi1(),
        exclusive_phi2()
    ]
