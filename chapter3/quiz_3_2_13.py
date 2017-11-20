from GF2 import one
from vec import Vec
from vecutil import zero_vec

def standard(D, one=one):
    """
    :param D: domain
    :param one: field to populate specifier
    :return: list of standard generators for Reals**D

    >>> D = set(range(3))
    >>> standard(D)
    [Vec({0, 1, 2},{0: one, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: one, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: one})]
    """
    return [zero_vec(D) + Vec(D, {member: one}) for member in D]
