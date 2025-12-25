# Source/exclusive_modified_automata.py

from Source.dfa_definitions import get_all_dfas
from Source.exclusive_modify import modify_for_exclusive_n


def get_all_exclusive_modified():
    """
    Returns exclusive-modified DFAs for ALL properties.
    """
    dfas_with_deciding = get_all_dfas()
    modified = []

    for i, (dfa, own_deciding) in enumerate(dfas_with_deciding):
        others_deciding = set().union(
            *[ev for j, (_, ev) in enumerate(dfas_with_deciding) if j != i]
        )

        modified.append(
            modify_for_exclusive_n(dfa, own_deciding, others_deciding)
        )

    return modified
