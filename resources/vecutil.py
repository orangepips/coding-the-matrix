# Copyright 2013 Philip N. Klein
from resources.vec import Vec

def list2vec(L):
    """Given a list L of field elements, return a Vec with domain {0...len(L)-1}
    whose entry i is L[i]

    >>> list2vec([10, 20, 30])
    Vec({0, 1, 2},{0: 10, 1: 20, 2: 30})
    """
    return Vec(set(range(len(L))), {k:L[k] for k in range(len(L))})

def zero_vec(D):
    """Returns a zero vector with the given domain
    """
    return Vec(D, {})


def vec2list(v):
    """
    Given an n vector with domain D return an n list of values in order of sorted(D)
    :param v: n vector
    :return: n list
    """
    return [v[d] for d in sorted(v.D)]