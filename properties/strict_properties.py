from helper.product import DFA

def build_strict_properties():
    states = ['start', 'right', 'left']

    def d(q, a):
        if a == 'r':
            return 'right'
        if a == 'l':
            return 'left'
        return q

    alphabet = ['r', 'l']

    props = []

    props.append(
        DFA("φ1", alphabet, states, 'start',
            lambda q: q == 'right', d, ['right'])
    )

    props.append(
        DFA("φ2", alphabet, states, 'start',
            lambda q: q == 'left', d, ['left'])
    )

    props.append(
        DFA("φ3", alphabet, states, 'start',
            lambda q: q == 'start', d, ['start'])
    )

    props.append(
        DFA("φ4", alphabet, states, 'start',
            lambda q: q != 'left', d, ['start', 'right'])
    )

    return props
