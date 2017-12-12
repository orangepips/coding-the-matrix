from GF2 import one
from vecutil import list2vec
from vec import Vec
from math import pi, sqrt
from vecutil import zero_vec


def zero_vec_n(n):
    return zero_vec(set(list(range(n))))

def lin_comb_sum(scalars, vectors):
    return sum([s*v for s, v in zip(scalars, vectors)])


def problem_5_14_1(a, b, c):
    """
    Multiply the vectors in V span by the scalars a, b, c
    :param a: scalar
    :param b: scalar
    :param c: scalar
    :return: sum of the span vectors multiplied by a, b and c

    >>> problem_5_14_1(1,1,0) == list2vec([2,1,4,1]) # a
    True
    >>> problem_5_14_1(1/2, 1, 1) == list2vec([1,1,1,0]) # b
    True
    >>> problem_5_14_1(0,1,-1) == list2vec([0,1,1,2]) # c
    True
    """
    V = [list2vec([2,0,4,0]), list2vec([0,1,0,1]), list2vec([0,0,-1,-1])]
    #return a * V[0] + b * V[1] + c * V[2]
    return lin_comb_sum([a, b, c], V)


def problem_5_14_2(a, b, c):
    """
    Multiply the vectors in V span by the scalars a, b, c
    :param a: scalar
    :param b: scalar
    :param c: scalar
    :return: sum of the span vectors multiplied by a, b and c

    >>> problem_5_14_2(3,-1,1) == list2vec([2,1,4]) # a
    True
    >>> problem_5_14_2(1/2,-3/2,1) == list2vec([1,1,1]) # b
    True
    >>> problem_5_14_2(1/2,-11/2,4) == list2vec([5,4,3]) # c
    True
    >>> problem_5_14_2(1,-2,1) == list2vec([0,1,1]) # d
    True
    """
    V = [list2vec([0,0,1]),list2vec([2,0,1]),list2vec([4,1,2])]
    # return a * V[0] + b * V[1] + c * V[2]
    return lin_comb_sum([a, b, c], V)


def problem_5_14_3(a, b, c, d):
    """
    Multiply the vectors in V span by the scalars a, b, c and d
    :param a: scalar
    :param b: scalar
    :param c: scalar
    :param d: scalar
    :return: sum of the span vectors multiplied by  a, b, c and d

    >>> problem_5_14_3(one,0,one,0) == list2vec([one,one,0,0]) # a
    True
    >>> problem_5_14_3(one,0,0,one) == list2vec([one,0,one,0]) # b
    True
    >>> problem_5_14_3(one,one,0,one) == list2vec([one,0,0,0]) # c
    True
    """
    V = [list2vec([0,one,0,one]), list2vec([0,0,one,0]), list2vec([one,0,0,one]), list2vec([one,one,one,one])]
    # return a * V[0] + b * V[1] + c * V[2] + d * V[3]
    return lin_comb_sum([a, b, c, d], V)


D_5_14_4 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
V_5_14_4 = {
    'v1': Vec(D_5_14_4, {'a':one, 'b':one}),
    'v2': Vec(D_5_14_4, {'b':one, 'c':one}),
    'v3': Vec(D_5_14_4, {'a':one, 'd':one}),
    'v4': Vec(D_5_14_4, {'b':one, 'e':one}),
    'v5': Vec(D_5_14_4, {'c':one, 'e':one}),
    'v6': Vec(D_5_14_4, {'d':one, 'e':one}),
    'v7': Vec(D_5_14_4, {'f':one, 'h':one}),
    'v8': Vec(D_5_14_4, {'g':one, 'h':one})
}
def problem_5_14_4(edges):
    """
    :param scalars: set of edges to follow
    :return: linear combination of scalars * V

    >>> problem_5_14_4({'v5', 'v6'}) == Vec(D_5_14_4, {'c': one, 'd': one})
    True
    >>> problem_5_14_4({'v7', 'v8'}) == Vec(D_5_14_4, {'f': one, 'g': one})
    True
    >>> problem_5_14_4({'v3', 'v6'}) == Vec(D_5_14_4, {'a': one, 'e': one})
    True
    >>> problem_5_14_4({'v1', 'v3'}) == Vec(D_5_14_4, {'b': one, 'd': one})
    True
    """
    V = V_5_14_4
    return sum([one * V[edge] for edge in edges])

zero_vec_3 = zero_vec_n(3)

def problem_5_14_5(scalars, vectors):
    """
    Linear combination of scalars and vectors
    :param scalars: n list of scalars
    :param vectors: n list of vectors
    :return: linear combination of scalar[i] * vector[i]

    >>> a_vectors = [list2vec([1,2,0]), list2vec([2,4,1]), list2vec([0,0,-1])]
    >>> problem_5_14_5([-2,1,1], a_vectors) == zero_vec_3
    True
    >>> b_vectors = [list2vec([2,4,0]), list2vec([8,16,4]), list2vec([0,0,7])]
    >>> problem_5_14_5([-4, 1, -4/7], b_vectors) == zero_vec_3
    True
    >>> c_vectors = [list2vec([0,0,5]), list2vec([1,34,2]), list2vec([123,456,789]), list2vec([-3,-6,0]), list2vec([1,2,0.5])]
    >>> problem_5_14_5([-3/10,0,0,1,3], c_vectors) == zero_vec_3
    True
    """
    return lin_comb_sum(scalars, vectors)

def problem_5_14_6(scalars, vectors):
    """
    Linear combination of scalars and vectors
    :param scalars: n list of scalars
    :param vectors: n list of vectors
    :return: linear combination of scalar[i] * vector[i]

    >>> a_vectors = [list2vec([1,2,3]), list2vec([4,5,6]), list2vec([1,1,1])]
    >>> problem_5_14_6([-1,1,-3], a_vectors) == zero_vec_3
    True
    >>> b_vectors = [list2vec([0,-1,0,-1]), list2vec([pi, pi, pi, pi]), list2vec([-sqrt(2), sqrt(2), -sqrt(2), sqrt(2)])]
    >>> problem_5_14_6([2*sqrt(2), sqrt(2)/pi, 1], b_vectors) == zero_vec_n(4)
    True
    >>> c_vectors = [list2vec([1,-1,0,0,0]), list2vec([0,1,-1,0,0]), list2vec([0,0,1,-1,0]), list2vec([0,0,0,1,-1]), list2vec([-1,0,0,0,1])]
    >>> problem_5_14_6([1,1,1,1,1], c_vectors) == zero_vec_n(5)
    True
    """
    return lin_comb_sum(scalars, vectors)

def problem_5_14_7(scalars, vectors):
    """
    >>> u = list2vec([3, 9, 6, 5, 5])
    >>> v = list2vec([4, 10, 6, 6, 8])
    >>> w = list2vec([1, 1, 0, 1, 3])
    >>> problem_5_14_6([-1, 1], [u, v]) == w
    True
    """
    return lin_comb_sum(scalars, vectors)

def problem_5_14_8(scalars, vectors):
    """
    >>> u = list2vec([1,1,0,0])
    >>> v = list2vec([0,1,1,0])
    >>> w = list2vec([0,0,1,1])
    >>> x = list2vec([1,0,0,1])
    >>> problem_5_14_8([1, -1, 1], [u, v, w]) == x
    True
    >>> problem_5_14_8([-1, 1, 1], [u, v, x]) == w
    True
    >>> problem_5_14_8([1, 1, -1], [u, w, x]) == v
    True
    >>> problem_5_14_8([1, -1, 1], [v, w, x]) == u
    True
    """
    return lin_comb_sum(scalars, vectors)


def list_of_lists_to_vecs(list_of_lists):
    return [list2vec(l) for l in list_of_lists]


def problem_5_14_9(scalars, vectors):
    """
    Problem c cutoff in Kindle edition. Using value from Coursera course:
    https://github.com/jimcarson/Coursera/blob/master/CodingTheMatrix/hw12_basis_problems/The_Basis_problems.py#L118

    >>> zero_vec_4 = zero_vec_n(4)
    >>> a_vectors = list_of_lists_to_vecs([[one, one, one, one], [one, 0, one, 0], [0, one, one, 0], [0, one, 0, one]])
    >>> problem_5_14_9([one, one, 0, one], a_vectors) == zero_vec_4
    True
    >>> b_vectors = list_of_lists_to_vecs([[0, 0, 0, one], [0, 0, one, 0], [one, one, 0, one], [one, one, one, one]])
    >>> problem_5_14_9([0, one, one, one], b_vectors) == zero_vec_4
    True
    >>> c_vectors = list_of_lists_to_vecs([[one,one,0,one,one], [0,0,one,0,0], [0,0,one,one,one], [one,0,one,one,one], [one,one,one,one,one]])
    >>> problem_5_14_9([one, one, 0, 0, one], c_vectors) == list2vec([0, 0, 0, 0, 0])
    True
    """
    return lin_comb_sum(scalars, vectors)

#      a     b    c    d    e    f    g    h
# v1   one   one
# v2         one  one
# v3   one             one
# v4         one            one
# v5              one       one
# v6                   one  one
# v7                             one       one
# v8                                  one  one


def problem_5_4_10(scalars, vectors):
    """
    >>> zero_vec_D_5_14_4 = zero_vec(D_5_14_4)
    >>> a_vectors = [V_5_14_4[key] for key in ['v1', 'v2', 'v3', 'v4', 'v5']]
    >>> problem_5_4_10([0, one, 0, one, one], a_vectors) == zero_vec_D_5_14_4
    True
    >>> b_vectors = [V_5_14_4[key] for key in ['v1', 'v2', 'v3', 'v4', 'v5', 'v7', 'v8']]
    >>> problem_5_4_10([0, one, 0, one, one, 0, 0], b_vectors) == zero_vec_D_5_14_4
    True
    >>> c_vectors = [V_5_14_4[key] for key in ['v1', 'v2', 'v3', 'v4', 'v6']]
    >>> problem_5_4_10([one, 0, one, one, one], c_vectors) == zero_vec_D_5_14_4
    True
    >>> d_vectors = [V_5_14_4[key] for key in ['v1', 'v2', 'v3', 'v5', 'v6', 'v7', 'v8']]
    >>> problem_5_4_10([one, one, one, one, one, 0, 0], d_vectors) == zero_vec_D_5_14_4
    True
    """
    return lin_comb_sum(scalars, vectors)


S_5_14_11 = {ix:list2vec(l) for ix, l in enumerate([
                     # w
    [1, 0, 0, 0, 0], # 0
    [0, 1, 0, 0, 0], # 1
    [0, 0, 1, 0, 0], # 2
    [0, 0, 0, 1, 0], # 3
    [0, 0, 0, 0, 1]  # 4
])}


def problem_5_14_11(scalars, w, z):
    """
    The Exchange Lemma is defined in 5.11
    :param scalars: list of ints
    :param w: vector key in S, but not in A, to replace with z
    :param z: vector to replace vector in position w
    :return: linear combination of scalars over the union of S and {z} minus {w}
    >>>
    >>>

    >>> a_z = list2vec([1, 1, 1, 1, 1])
    >>> a_w = 4
    >>> problem_5_14_11([-1, -1, -1, -1, 1], a_w, a_z) == S_5_14_11[a_w] # [0, 0, 0, 0, 1]
    True
    >>> b_z = list2vec([0, 1, 0, 1, 0])
    >>> b_w = 3
    >>> problem_5_14_11([0, -1, 0, 1, 0], b_w, b_z) == S_5_14_11[b_w] # [0, 0, 0, 1, 0]
    True
    >>> c_z = list2vec([1, 0, 1, 0, 1])
    >>> c_w = 2
    >>> problem_5_14_11([-1, 0, 1, 0, -1], c_w, c_z) == S_5_14_11[c_w] # [0, 0, 1, 0, 0]
    True
    """
    S = S_5_14_11.copy()
    A = {0, 1}
    assert w in S
    assert w not in A
    S[w] = z
    return lin_comb_sum(scalars, [S[key] for key in sorted(S.keys())])


#      a     b    c    d    e    f    g    h
# v1   one   one
# v2         one  one
# v3   one             one
# v4         one            one
# v5              one       one
# v6                   one  one
# v7                             one       one
# v8                                  one  one
def problem_5_14_12(scalars, w, z, A, S=None):
    """
    :param scalars: S len list of scalars to multiple S by
    :param w: key in S to replace with z
    :param z: vector to replace key w in S with
    :param A: set of keys in S to retain
    :param S: dictionary of vectors
    :return: linear combination of scalars * S in dictionary key order
    >>> a_A = {'v1', 'v4'}
    >>> a_w = 'v6'
    >>> a_z = Vec(D_5_14_4, {'d': one, 'e': one})
    >>> problem_5_14_12([0, 0, 0, 0, 0, one, 0, 0], a_w, a_z, a_A) == V_5_14_4[a_w] # {'d': one, 'e': one}
    True
    >>> b_A = {'v2', 'v3'}
    >>> b_w = 'v5'
    >>> b_z = Vec(D_5_14_4, {'c': one, 'd': one})
    >>> problem_5_14_12([0, one, 0, one, 0, 0, 0, 0], b_w, b_z, b_A) == V_5_14_4[b_w] # {'c': one, 'e': one}
    True
    >>> c_A = {'v2', 'v3'}
    >>> c_w = 'v4'
    >>> c_z = Vec(D_5_14_4, {'a': one, 'e': one})
    >>> problem_5_14_12([0, one, 0, 0, one, 0, 0, 0], c_w, c_z, c_A) == V_5_14_4[c_w] # {'b': one, 'e': one}
    True
    """
    S = V_5_14_4.copy() if S is None else S
    assert w in S
    assert w not in A
    S[w] = z
    return lin_comb_sum(scalars, [S[key] for key in sorted(S.keys())])


