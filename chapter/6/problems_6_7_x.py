from resources.GF2 import one
from resources.vecutil import list2vec

w0 = list2vec([1,0,0])
w1 = list2vec([0,1,0])
w2 = list2vec([0,0,1])

v0 = list2vec([1,2,3])
v1 = list2vec([1,3,3])
v2 = list2vec([0,3,3])


def lin_comb_sum(scalars, vectors):
    '''
    :param scalars: n length list of scalars
    :param vectors: n length list of m length vectors
    :return: m length vector linear combination of scalars * vectors
    # 6.7.2
    >>> w0 = list2vec([1,0,0])
    >>> w1 = list2vec([0,1,0])
    >>> w2 = list2vec([0,0,1])

    >>> v0 = list2vec([1,2,3])
    >>> v1 = list2vec([1,3,3])
    >>> v2 = list2vec([0,3,3])
    >>> lin_comb_sum([1, -2, -3], [v0, w1, w2]) == w0 # v0 & w0
    True
    >>> lin_comb_sum([-1, 1, 0], [v0, v1, w2]) == w1 # v1 & w1
    True
    >>> lin_comb_sum([1, -1, 1/3], [v0, v1, v2]) == w2 # v2 & w2
    True

    # 6.7.3
    >>> w0 = list2vec([0,one,0])
    >>> w1 = list2vec([0,0,one])
    >>> w2 = list2vec([one,one,one])

    >>> v0 = list2vec([one,0,one])
    >>> v1 = list2vec([one,0,0])
    >>> v2 = list2vec([one,one,0])
    >>> lin_comb_sum([0, one, one], [w0, w2, v2]) == w1 # w1 & v2
    True
    >>> lin_comb_sum([one, one, 0], [v0, w2, v2]) == w0 # w0 & v0
    True
    >>> lin_comb_sum([one, one, one], [v0, v1, v2]) == w2 # w2 & v1
    True
    '''
    return sum([s*v for s, v in zip(scalars, vectors)])


def only_share_zero_vec(U, V):
    '''
    Determine if the intersection of U and V are equivalent to the zero set
    :param U: set of n vectors
    :param V: set of n vectors not overlapping U
    :return: True if U & V do not overlap

    # 6.7.9
    >>> u1 = {list2vec([one, 0, one, 0]), list2vec([0, 0, one, 0])}
    >>> v1 = {list2vec(([0, one, 0, one])), list2vec([0, 0, 0, one])}
    >>> only_share_zero_vec(v1, u1)
    True
    >>> u2 = {list2vec([1, 2, 3]), list2vec([1, 2, 0])}
    >>> v2 = {list2vec([2, 1, 3]), list2vec([2, 1, 3])}
    >>> only_share_zero_vec(v1, u1)
    True
    >>> u3 = {list2vec([2, 0, 8, 0]), list2vec([1, 1, 4, 0])}
    >>> v3 = {list2vec([2, 1, 1, 1]), list2vec([0, 1, 1, 1])}
    >>> only_share_zero_vec(u3, v3)
    True
    '''
    from grading.The_Basis_problems import exchange
    U_copy = U.copy()
    for inserted in V:
        ejected = exchange(list(U_copy), list(V), inserted)
        # print('Inserted: {0}\tEjected: {1}'.format(inserted, ejected))
        if ejected is not None: return False

    return True