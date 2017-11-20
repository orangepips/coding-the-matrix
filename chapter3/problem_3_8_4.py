from vec import Vec
from chapter3.quiz_3_1_7 import lin_comb

def problem_3_8_4(vlist, clist):
    '''
    a & b are real numbers
    z = ax + by
    ax + by - z = 0
    Prove there are 2 3-vectors v1 & v2 such that points [x, y, z]
    satisfying the equation is exactly the set of linear combinations of v1 & v2
    :param vlist: list of vectors
    :param clist: list of scalars same length as vlist
    :return: linear combination of the passed vectors and scalars

    >>> D = {'x', 'y', 'z'}
    >>> v1 = Vec(D, {'x': 1, 'y': -1})
    >>> v2 = Vec(D, {'x': -1, 'y': 1})
    >>> clist = [1, 1] # a, b
    >>> lin_comb([v1, v2], clist) == Vec(D, {})
    True
    '''
    return lin_comb(vlist, clist)