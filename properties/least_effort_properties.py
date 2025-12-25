from helper.product import DFA

def build_least_effort_properties(n):
    props = []
    alphabet = ['r', 'l']
    states = ['start', 'r_seen', 'l_seen']

    def d(q, a):
        if a == 'r': return 'r_seen'
        if a == 'l': return 'l_seen'
        return q

    for i in range(n):
        props.append(
            DFA(
                f"LE_phi_{i}",
                alphabet,
                states,
                'start',
                lambda q, i=i: q in ['r_seen', 'l_seen'],
                d,
                ['r_seen', 'l_seen']
            )
        )
    return props
