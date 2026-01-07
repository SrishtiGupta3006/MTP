# dfa_definitions.py

from helper.product import DFA as PropertyDFA
from helper.Automata import DFA as ExclusiveDFA    # For Exclusive properties

# ======================================================
# STRICT SERIAL PROPERTY DFAs
# ======================================================

def strict_serial_transitions():

    return {
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


def Strict_serial_phi1():
    
    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_serial_transitions()

    return PropertyDFA(
        "phi1",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'right',
        lambda q, a: transition_dict[(q, a)],
        ['right']
    )


def Strict_serial_phi2():
    
    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_serial_transitions()

    return PropertyDFA(
        "phi2",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'left',
        lambda q, a: transition_dict[(q, a)],
        ['left']
    )

def Strict_serial_phi3():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_serial_transitions()

    return PropertyDFA(
        "phi3",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'back',          
        lambda q, a: transition_dict[(q, a)],
        ['back']
    )

def Strict_serial_phi4():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_serial_transitions()

    return PropertyDFA(
        "phi4",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'forward',
        lambda q,a: transition_dict[(q,a)],
        ['forward']
    )

def Strict_serial_phi5():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_serial_transitions()

    return PropertyDFA(
        "phi5",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q in {'back','left'},
        lambda q, a: transition_dict[(q, a)],
        ['back', 'left']
    )

def Strict_serial_phi6():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_serial_transitions()

    return PropertyDFA(
        "phi6",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q in {'forward','left'},
        lambda q, a: transition_dict[(q, a)],
        ['forward','left']
    )

def Strict_serial_phi7():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_serial_transitions()

    return PropertyDFA(
        "phi7",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q in {'right','left'},
        lambda q, a: transition_dict[(q, a)],
        ['right','left']
    )

def Strict_serial_phi8():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_serial_transitions()

    return PropertyDFA(
        "phi8",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q in {'start','left'},
        lambda q, a: transition_dict[(q, a)],
        ['start','left']
    )


def get_all_Strict_serial_dfas():
    
    return [
        Strict_serial_phi1(),
        Strict_serial_phi2(),
        Strict_serial_phi3(),
        Strict_serial_phi4(),
        Strict_serial_phi5(),
        Strict_serial_phi6(),
        Strict_serial_phi7(),
        Strict_serial_phi8(),
    ]

# ======================================================
# STRICT MONOLITHIC PROPERTY DFAs
# ======================================================

def strict_mono_transitions():

    return {
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

def Strict_mono_phi1():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_mono_transitions()

    return PropertyDFA(
        "phi1",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q in {'right', 'left'},
        lambda q, a: transition_dict[(q, a)],
        []
    )


def Strict_mono_phi2():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_mono_transitions()

    return PropertyDFA(
        "phi2",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q:q == 'left',
        lambda q, a: transition_dict[(q, a)],
        []
    )


def Strict_mono_phi3():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_mono_transitions()

    return PropertyDFA(
        "phi3",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q in {'forward', 'left'} ,
        lambda q, a: transition_dict[(q, a)],
        []
    )

def Strict_mono_phi4():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_mono_transitions()

    return PropertyDFA(
        "phi4",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q in {'back', 'left'} ,
        lambda q, a: transition_dict[(q, a)],
        []
    )

def Strict_mono_phi5():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_mono_transitions()

    return PropertyDFA(
        "phi5",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'right',
        lambda q, a: transition_dict[(q, a)],
        []
    )

def Strict_mono_phi6():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_mono_transitions()

    return PropertyDFA(
        "phi6",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'left',
        lambda q, a: transition_dict[(q, a)],
        []
    )

def Strict_mono_phi7():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_mono_transitions()

    return PropertyDFA(
        "phi7",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'forward',
        lambda q, a: transition_dict[(q, a)],
        []
    )

def Strict_mono_phi8():

    states = ['start', 'right', 'left', 'forward', 'back', 'stop']
    transition_dict = strict_mono_transitions()

    return PropertyDFA(
        "phi8",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'back',
        lambda q, a: transition_dict[(q, a)],
        []
    )

def get_all_Strict_mono_dfas():

    return [
        Strict_mono_phi1(),
        Strict_mono_phi2(),
        Strict_mono_phi3(),
        Strict_mono_phi4(),
        Strict_mono_phi5(),
        Strict_mono_phi6(),
        Strict_mono_phi7(),
        Strict_mono_phi8(),
    ]


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

def Strict_parallel_phi3():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = strict_parallel_transitions()

    return PropertyDFA(
        "phi3",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'back',
        lambda q, a: transition_dict[(q, a)],
        ['back']
    )

def Strict_parallel_phi4():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = strict_parallel_transitions()

    return PropertyDFA(
        "phi4",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q == 'forward',
        lambda q, a: transition_dict[(q, a)],
        ['forward']
    )

def Strict_parallel_phi5():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = strict_parallel_transitions()

    return PropertyDFA(
        "phi5",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q in {'right','left'},
        lambda q, a: transition_dict[(q, a)],
        ['right', 'left']
    )

def Strict_parallel_phi6():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = strict_parallel_transitions()

    return PropertyDFA(
        "phi6",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q in {'right','back'},
        lambda q, a: transition_dict[(q, a)],
        ['right', 'back']
    )

def Strict_parallel_phi7():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = strict_parallel_transitions()

    return PropertyDFA(
        "phi7",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q in {'right','forward'},
        lambda q, a: transition_dict[(q, a)],
        ['right','forward']
    )

def Strict_parallel_phi8():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = strict_parallel_transitions()

    return PropertyDFA(
        "phi8",
        ['r','l','f','b','s'],
        states,
        'start',
        lambda q: q in {'left','back'},
        lambda q, a: transition_dict[(q, a)],
        ['left','back']
    )

def get_all_Strict_parallel_dfas():

    return [
        Strict_parallel_phi1(),
        Strict_parallel_phi2(),
        Strict_parallel_phi3(),
        Strict_parallel_phi4(),
        Strict_parallel_phi5(),
        Strict_parallel_phi6(),
        Strict_parallel_phi7(),
        Strict_parallel_phi8(),
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
        "phi1",
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
        "phi2",
        ['r', 'l', 'f', 'b', 's'],
        states,
        'start',
        lambda q: q in ['left'],
        lambda q, a: transition_dict[(q, a)],
        ['left']
    )

def LE_mono_phi3():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = LE_mono_transitions()

    return PropertyDFA(
        "phi3",
        ['r', 'l', 'f', 'b', 's'],
        states,
        'start',
        lambda q: q in ['back'],
        lambda q, a: transition_dict[(q, a)],
        ['back']
    )

def LE_mono_phi4():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = LE_mono_transitions()

    return PropertyDFA(
        "phi4",
        ['r', 'l', 'f', 'b', 's'],
        states,
        'start',
        lambda q: q in ['forward'],
        lambda q, a: transition_dict[(q, a)],
        ['forward']
    )

def LE_mono_phi5():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back']
    transition_dict = LE_mono_transitions()

    return PropertyDFA(
        "phi5",
        ['r', 'l', 'f', 'b', 's'],
        states,
        'start',
        lambda q: q in ['forward'],
        lambda q, a: transition_dict[(q, a)],
        ['forward']
    )


def get_all_LE_mono_dfas():

    return [
        LE_mono_phi1(),
        LE_mono_phi2(),
        LE_mono_phi3(),
        LE_mono_phi4(),
        LE_mono_phi5(),
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
        "phi1",
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
        "phi2",
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
        "phi3",
        ['r','l','f','b','s','u','d'],
        states,
        'start',
        lambda q: q in ['left', 'forward'],
        lambda q, a: transition_dict[(q, a)],
        ['left', 'forward']
    )

def LE_parallel_phi4():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back', 'up', 'down']
    transition_dict = LE_parallel_transitions()

    return PropertyDFA(
        "phi4",
        ['r','l','f','b','s','u','d'],
        states,
        'start',
        lambda q: q in ['left', 'up'],
        lambda q, a: transition_dict[(q, a)],
        ['left', 'up']
    )

def LE_parallel_phi5():

    states = ['stop', 'start', 'right', 'left', 'forward', 'back', 'up', 'down']
    transition_dict = LE_parallel_transitions()

    return PropertyDFA(
        "phi5",
        ['r','l','f','b','s','u','d'],
        states,
        'start',
        lambda q: q in ['left', 'up'],
        lambda q, a: transition_dict[(q, a)],
        ['left', 'up']
    )

def get_all_LE_parallel_dfas():

    return [
        LE_parallel_phi1(),
        LE_parallel_phi2(),
        LE_parallel_phi3(),
        LE_parallel_phi4(),
        LE_parallel_phi5()
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

# A3 : decides on 'r'
def exclusive_phi3():

    def d3(q, a):
        transitions = {
            "s0": {"r": "s1", "f": "s0", "l": "s0", "o": "s0", "n": "s0"},
            "s1": {"r": "s2", "f": "s1", "l": "s1", "o": "s1", "n": "s1"},
            "s2": {"f": "s2", "l": "s2", "o": "s2", "n": "s2", "r": "s2"},
        }
        return transitions[q].get(a, q)

    A3 = ExclusiveDFA(
        S={"f", "l", "o", "n", "r"},
        Q=["s0", "s1", "s2"],
        q0="s0",
        F=lambda q: q == "s2",
        d=d3
    )
    A3.name = "A3"

    return A3, {"r"}

# A4 : decides on 'o'
def exclusive_phi4():

    def d4(q, a):
        transitions = {
            "t0": {"o": "t1", "f": "t0", "l": "t0", "n": "t0", "r": "t0"},
            "t1": {"o": "t2", "f": "t1", "l": "t1", "n": "t1", "r": "t1"},
            "t2": {"f": "t2", "l": "t2", "o": "t2", "n": "t2", "r": "t2"},
        }
        return transitions[q].get(a, q)

    A4 = ExclusiveDFA(
        S={"f", "l", "o", "n", "r"},
        Q=["t0", "t1", "t2"],
        q0="t0",
        F=lambda q: q == "t2",
        d=d4
    )
    A4.name = "A4"

    return A4, {"o"}

# A5 : decides on 'f'
def exclusive_phi5():

    def d5(q, a):
        transitions = {
            "u0": {"f": "u1", "l": "u0", "o": "u0", "n": "u0", "r": "u0"},
            "u1": {"f": "u2", "l": "u1", "o": "u1", "n": "u1", "r": "u1"},
            "u2": {"f": "u2", "l": "u2", "o": "u2", "n": "u2", "r": "u2"},
        }
        return transitions[q].get(a, q)

    A5 = ExclusiveDFA(
        S={"f", "l", "o", "n", "r"},
        Q=["u0", "u1", "u2"],
        q0="u0",
        F=lambda q: q == "u2",
        d=d5
    )
    A5.name = "A5"

    return A5, {"f"}

# A6 : decides on 'r'
def exclusive_phi6():

    def d6(q, a):
        transitions = {
            "v0": {"r": "v1", "f": "v0", "l": "v0", "o": "v0", "n": "v0"},
            "v1": {"r": "v2", "f": "v1", "l": "v1", "o": "v1", "n": "v1"},
            "v2": {"r": "v2", "f": "v2", "l": "v2", "o": "v2", "n": "v2"},
        }
        return transitions[q].get(a, q)

    A6 = ExclusiveDFA(
        S={"f", "l", "o", "n", "r"},
        Q=["v0", "v1", "v2"],
        q0="v0",
        F=lambda q: q == "v2",
        d=d6
    )
    A6.name = "A6"

    return A6, {"r"}

# A7 : decides on 'o'
def exclusive_phi7():

    def d7(q, a):
        transitions = {
            "w0": {"o": "w1", "f": "w0", "l": "w0", "n": "w0", "r": "w0"},
            "w1": {"o": "w2", "f": "w1", "l": "w1", "n": "w1", "r": "w1"},
            "w2": {"o": "w2", "f": "w2", "l": "w2", "n": "w2", "r": "w2"},
        }
        return transitions[q].get(a, q)

    A7 = ExclusiveDFA(
        S={"f", "l", "o", "n", "r"},
        Q=["w0", "w1", "w2"],
        q0="w0",
        F=lambda q: q == "w2",
        d=d7
    )
    A7.name = "A7"

    return A7, {"o"}

# A8 : decides on 'n'
def exclusive_phi8():

    def d8(q, a):
        transitions = {
            "x0": {"n": "x1", "f": "x0", "l": "x0", "o": "x0", "r": "x0"},
            "x1": {"n": "x2", "f": "x1", "l": "x1", "o": "x1", "r": "x1"},
            "x2": {"n": "x2", "f": "x2", "l": "x2", "o": "x2", "r": "x2"},
        }
        return transitions[q].get(a, q)

    A8 = ExclusiveDFA(
        S={"f", "l", "o", "n", "r"},
        Q=["x0", "x1", "x2"],
        q0="x0",
        F=lambda q: q == "x2",
        d=d8
    )
    A8.name = "A8"

    return A8, {"n"}

# A9 : decides on 'l'
def exclusive_phi9():

    def d9(q, a):
        transitions = {
            "y0": {"l": "y1", "f": "y0", "o": "y0", "n": "y0", "r": "y0"},
            "y1": {"l": "y2", "f": "y1", "o": "y1", "n": "y1", "r": "y1"},
            "y2": {"l": "y2", "f": "y2", "o": "y2", "n": "y2", "r": "y2"},
        }
        return transitions[q].get(a, q)

    A9 = ExclusiveDFA(
        S={"f", "l", "o", "n", "r"},
        Q=["y0", "y1", "y2"],
        q0="y0",
        F=lambda q: q == "y2",
        d=d9
    )
    A9.name = "A9"
    return A9, {"l"}


# A10 : decides on 'n'
def exclusive_phi10():

    def d10(q, a):
        transitions = {
            "z0": {"n": "z1", "f": "z0", "l": "z0", "o": "z0", "r": "z0"},
            "z1": {"n": "z2", "f": "z1", "l": "z1", "o": "z1", "r": "z1"},
            "z2": {"n": "z2", "f": "z2", "l": "z2", "o": "z2", "r": "z2"},
        }
        return transitions[q].get(a, q)

    A10 = ExclusiveDFA(
        S={"f", "l", "o", "n", "r"},
        Q=["z0", "z1", "z2"],
        q0="z0",
        F=lambda q: q == "z2",
        d=d10
    )
    A10.name = "A10"
    return A10, {"n"}

# A11 : decides on 'r'
def exclusive_phi11():

    def d11(q, a):
        transitions = {
            "a0": {"r": "a1", "f": "a0", "l": "a0", "o": "a0", "n": "a0"},
            "a1": {"r": "a2", "f": "a1", "l": "a1", "o": "a1", "n": "a1"},
            "a2": {"r": "a2", "f": "a2", "l": "a2", "o": "a2", "n": "a2"},
        }
        return transitions[q].get(a, q)

    A11 = ExclusiveDFA(
        S={"f", "l", "o", "n", "r"},
        Q=["a0", "a1", "a2"],
        q0="a0",
        F=lambda q: q == "a2",
        d=d11
    )
    A11.name = "A11"
    return A11, {"r"}

def get_all_dfas():

    return [
        exclusive_phi1(),
        exclusive_phi2(),
        exclusive_phi3(),
        exclusive_phi4(),
        exclusive_phi5(),
        exclusive_phi6(),
        exclusive_phi7(),
        exclusive_phi8(),
        exclusive_phi9(),
        exclusive_phi10(),
        exclusive_phi11()
    ]

