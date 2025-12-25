import copy
from Source.exclusive_modified_automata import A1_mod, A2_mod

def build_exclusive_properties(k):
    """
    Builds k exclusive *pairs* (2k DFAs)
    """
    props = []
    for i in range(k):
        a1 = copy.deepcopy(A1_mod)
        a2 = copy.deepcopy(A2_mod)
        a1.name = f"A1_{i}"
        a2.name = f"A2_{i}"
        props.extend([a1, a2])
    return props
