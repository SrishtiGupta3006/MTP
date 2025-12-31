# dfa_definitions.py

from helper.product import DFA as PropertyDFA
from helper.Automata import DFA as ExclusiveDFA    # For Exclusive properties

# ======================================================
# STRICT PARALLEL PROPERTY DFAs
# ======================================================

def strict_parallel_transitions():
    return{
        ('start','r'):'right',
        ('start','l'):'left',
        ('start','f'):'forward',
        ('start','b'):'back',
        ('start','s'):'stop',

        ('right','r'):'right',
        ('right','l'):'left',
        ('right','f'):'forward',
        ('right','b'):'back',
        ('right','s'):'stop',

        ('left','r'):'right',
        ('left','l'):'left',
        ('left','f'):'forward',
        ('left','b'):'back',
        ('left','s'):'stop',

        ('forward','r'):'right',
        ('forward','l'):'left',
        ('forward','f'):'forward',
        ('forward','b'):'back',
        ('forward','s'):'stop',

        ('back','r'):'right',
        ('back','l'):'left',
        ('back','f'):'forward',
        ('back','b'):'back',
        ('back','s'):'stop',

        ('stop','r'):'stop', 
        ('stop','l'):'stop',
        ('stop','f'):'stop',
        ('stop','b'):'stop',
        ('stop','s'):'stop',
    
    }

def Strict_parallel_phi1():
    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = strict_parallel_transitions()

    return PropertyDFA(
        "phi1",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'right',
        lambda q, a: transition_dict[(q, a)],
        ['right']
    )


def Strict_parallel_phi2():
    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = strict_parallel_transitions()

    return PropertyDFA(
        "phi2",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'left',
        lambda q, a: transition_dict[(q, a)],
        ['left']
    )


def get_all_Strict_parallel_dfas():
    return [
        Strict_parallel_phi1(),
        Strict_parallel_phi2()
    ]


# ======================================================
# LEAST-EFFORT MONOLITHIC PROPERTY DFAs
# ======================================================

def LE_mono_transitions():
    return{
        ('start', 'r'): 'right',
        ('start', 'l'): 'left',
        ('start', 'f'): 'forward',
        ('start', 'b'): 'back',
        ('start', 's'): 'stop',

        ('right', 'r'): 'right',
        ('right', 'l'): 'left',
        ('right', 'f'): 'forward',
        ('right', 'b'): 'back',
        ('right', 's'): 'stop',

        ('left', 'r'): 'right',
        ('left', 'l'): 'left',
        ('left', 'f'): 'forward',
        ('left', 'b'): 'back',
        ('left', 's'): 'stop',

        ('forward', 'r'): 'right',
        ('forward', 'l'): 'left',
        ('forward', 'f'): 'forward',
        ('forward', 'b'): 'back',
        ('forward', 's'): 'stop',

        ('back', 'r'): 'right',
        ('back', 'l'): 'left',
        ('back', 'f'): 'forward',
        ('back', 'b'): 'back',
        ('back', 's'): 'stop',

        ('stop', 'r'): 'stop',
        ('stop', 'l'): 'stop',
        ('stop', 'f'): 'stop',
        ('stop', 'b'): 'stop',
        ('stop', 's'): 'stop',
    }

def LE_mono_phi1():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = LE_mono_transitions()

    return PropertyDFA(
        "Property1",
        ['r', 'l', 'f', 'b', 's'],
        states,
        'start',
        lambda q: q in ['right'],
        lambda q, a: transition_dict[(q, a)],
        ['right']
    )


def LE_mono_phi2():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = LE_mono_transitions()

    return PropertyDFA(
        "Property2",
        ['r', 'l', 'f', 'b', 's'],
        states,
        'start',
        lambda q: q in ['left'],
        lambda q, a: transition_dict[(q, a)],
        ['left']
    )


def get_all_LE_mono_dfas():
    return [
        LE_mono_phi1(),
        LE_mono_phi2()
    ]


# ======================================================
# LEAST-EFFORT PARALLEL PROPERTY DFAs
# ======================================================

def LE_parallel_transitions():
    return {
        ('start','r'):'right',
        ('start','l'):'left',
        ('start','f'):'forward',
        ('start','b'):'back',
        ('start','u'):'up',
        ('start','d'):'down',
        ('start','s'):'stop',

        ('right','r'):'right',
        ('right','l'):'left',
        ('right','f'):'forward',
        ('right','b'):'back',
        ('right','u'):'up',
        ('right','d'):'down',
        ('right','s'):'stop',

        ('left','r'):'right',
        ('left','l'):'left',
        ('left','f'):'forward',
        ('left','b'):'back',
        ('left','u'):'up',
        ('left','d'):'down',
        ('left','s'):'stop',

        ('forward','r'):'right',
        ('forward','l'):'left',
        ('forward','f'):'forward',
        ('forward','b'):'back',
        ('forward','u'):'up',
        ('forward','d'):'down',
        ('forward','s'):'stop',

        ('back','r'):'right',
        ('back','l'):'left',
        ('back','f'):'forward',
        ('back','b'):'back',
        ('back','u'):'up',
        ('back','d'):'down',
        ('back','s'):'stop',

        ('up','r'):'right',
        ('up','l'):'left',
        ('up','f'):'forward',
        ('up','b'):'back',
        ('up','u'):'up',
        ('up','d'):'down',
        ('up','s'):'stop',

        ('down','r'):'right',
        ('down','l'):'left',
        ('down','f'):'forward',
        ('down','b'):'back',
        ('down','u'):'up',
        ('down','d'):'down',
        ('down','s'):'stop',

        ('stop','r'):'stop',
        ('stop','l'):'stop',
        ('stop','f'):'stop',
        ('stop','b'):'stop',
        ('stop','u'):'up',
        ('stop','d'):'down',
        ('stop','s'):'stop',
    }

def LE_parallel_phi1():
    states = ['stop', 'start', 'right', 'left', 'forward', 'back', 'up', 'down']
    transition_dict = LE_parallel_transitions()

    return PropertyDFA(
        "Property1",
        ['r','l','f','b','s','u','d'],
        states,
        'start',
        lambda q: q in ['right'],
        lambda q, a: transition_dict[(q, a)],
        ['right']
    )

def LE_parallel_phi2():
    states = ['stop', 'start', 'right', 'left', 'forward', 'back', 'up', 'down']
    transition_dict = LE_parallel_transitions()

    return PropertyDFA(
        "Property2",
        ['r','l','f','b','s','u','d'],
        states,
        'start',
        lambda q: q in ['right', 'left'],
        lambda q, a: transition_dict[(q, a)],
        ['right', 'left']
    )

def LE_parallel_phi3():
    states = ['stop', 'start', 'right', 'left', 'forward', 'back', 'up', 'down']
    transition_dict = LE_parallel_transitions()

    return PropertyDFA(
        "Property3",
        ['r','l','f','b','s','u','d'],
        states,
        'start',
        lambda q: q in ['left', 'forward'],
        lambda q, a: transition_dict[(q, a)],
        ['left', 'forward']
    )


def get_all_LE_parallel_dfas():
    return [
        LE_parallel_phi1(),
        LE_parallel_phi2(),
        LE_parallel_phi3()
    ]


# ======================================================
# EXCLUSIVE PROPERTY DFAs
# ======================================================

# A1 : decides on 'l'
def exclusive_phi1():
    def d1(q, a):
        transitions = {
            "q0": {"f": "q1", "l": "q0", "o": "q0", "n": "q0", "r": "q0"},
            "q1": {"l": "q2", "f": "q1", "o": "q1", "n": "q1", "r": "q1"},
            "q2": {"f": "q1", "l": "q2", "o": "q2", "n": "q2", "r": "q2"},
        }
        return transitions[q].get(a, q)

    A1 = ExclusiveDFA(
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

    A2 = ExclusiveDFA(
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

