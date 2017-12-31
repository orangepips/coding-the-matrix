from resources.matutil import identity
from resources.vecutil import list2vec
from resources.GF2 import one

def problem_6_13_13(S, T, scalars):
    '''
    >>> R_std_basis = identity(set(range(3)), 1)
    >>> S_1 = {list2vec([2, one, 2]), list2vec([one, one, one])}
    >>> T_1 = {list2vec([one, 0, 0])}
    >>> scalars_1__0_0_1 = {list2vec([2, one, 2]): one, list2vec([one, one, one]): -one, list2vec([one, 0, 0]): -1}
    >>> scalars_1__0_1_0 = {list2vec([2, one, 2]): -one, list2vec([one, one, one]): 2, list2vec([one, 0, 0]): 0}
    >>> scalars_1__1_0_0 = {list2vec([2, one, 2]): 0, list2vec([one, one, one]): 0, list2vec([one, 0, 0]): 1}
    >>> problem_6_13_13(S_one, T_one, scalars_1__0_0_1) == list2vec([0, 0, one])
    True
    >>> problem_6_13_13(S_one, T_one, scalars_1__0_1_0) == list2vec([0, one, 0])
    True
    >>> problem_6_13_13(S_one, T_one, scalars_1__1_0_0) == list2vec([one, 0, 0])
    True

    >>> S_2 = {list2vec([0, one, -one]), list2vec([0, 0, 0])}
    >>> T_2 = {list2vec([one, 0, 0]), list2vec([0, 0, one])}
    >>> scalars_2__0_0_1 = {list2vec([0, one, -one]): 0, list2vec([0, 0, 0]): 0, list2vec([one, 0, 0]): 0, list2vec([0, 0, one]): 1}
    >>> scalars_2__0_1_0 = {list2vec([0, one, -one]): one, list2vec([0, 0, 0]): 0, list2vec([one, 0, 0]): 0, list2vec([0, 0, one]): 1}
    >>> scalars_2__1_0_0 = {list2vec([0, one, -one]): 0, list2vec([0, 0, 0]): 0, list2vec([one, 0, 0]): one, list2vec([0, 0, one]): 0}
    >>> problem_6_13_13(S_2, T_2, scalars_2__0_0_1) == list2vec([0, 0, one])
    True
    >>> problem_6_13_13(S_2, T_2, scalars_2__0_1_0) == list2vec([0, one, 0])
    True
    >>> problem_6_13_13(S_2, T_2, scalars_2__1_0_0) == list2vec([one, 0, 0])
    True
    '''
    return lin_comb_2_sets(S, T, scalars)


def problemn_6_13_14(S, T, scalars):
    '''
    >>> S_1 = {list2vec([one, one, 0]), list2vec([0, one, one])}
    >>> T_1 = {list2vec([one, 0, 0])}
    >>> scalars_1__0_0_1 = {list2vec([one, one, 0]): one, list2vec([0, one, one]): one, list2vec([one, 0, 0]): one}
    >>> scalars_1__0_1_0 = {list2vec([one, one, 0]): one, list2vec([0, one, one]): 0, list2vec([one, 0, 0]): one}
    >>> scalars_1__1_0_0 = {list2vec([one, one, 0]): 0, list2vec([0, one, one]): 0, list2vec([one, 0, 0]): one}
    >>> problemn_6_13_14(S_1, T_1, scalars_1__0_0_1) == list2vec([0, 0, one])
    True
    >>> problemn_6_13_14(S_1, T_1, scalars_1__0_1_0) == list2vec([0, one, 0])
    True
    >>> problemn_6_13_14(S_1, T_1, scalars_1__1_0_0) == list2vec([one, 0, 0])
    True
    
    >>> S_2 = {list2vec([one, one, one])}
    >>> T_2 = {list2vec([one, one, 0]), list2vec([one, 0, 0])}
    >>> scalars_2__0_0_1 = {list2vec([one, one, one]): one, list2vec([one, one, 0]): one, list2vec([one, 0, 0]): 0}
    >>> scalars_2__0_1_0 = {list2vec([one, one, one]): 0, list2vec([one, one, 0]): one, list2vec([one, 0, 0]): one}
    >>> scalars_2__1_0_0 = {list2vec([one, one, one]): 0, list2vec([one, one, 0]): 0, list2vec([one, 0, 0]): one}
    >>> problemn_6_13_14(S_2, T_2, scalars_2__0_0_1) == list2vec([0, 0, one])
    True
    >>> problemn_6_13_14(S_2, T_2, scalars_2__0_1_0) == list2vec([0, one, 0])
    True
    >>> problemn_6_13_14(S_2, T_2, scalars_2__1_0_0) == list2vec([one, 0, 0])
    True
    '''
    return lin_comb_2_sets(S, T, scalars)


def lin_comb_2_sets(S, T, scalars):
    '''
    Multiply vectors in S and T by ints in scalars and sum as a linear combination
    :param S: a set of  n vectors
    :param T: a set of n vectors not in S
    :param scalars: dict of keys equal to S & T vectors and values as ints
    :return: linear combination n vector.
    '''
    assert S & T == set()
    assert S | T == scalars.keys()

    return sum([scalars[v] * v for v in list(S | T)])
