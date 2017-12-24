# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from vecutil import list2vec, zero_vec
from GF2 import one
from solver import solve
from matutil import listlist2mat, coldict2mat, mat2coldict, mat2rowdict, identity
from mat import Mat
from vec import Vec
from pprint import pprint
from independence import rank, is_independent
from triangular import triangular_solve


## 1: (Problem 6.7.2) Iterative Exchange Lemma
w0 = list2vec([1,0,0])
w1 = list2vec([0,1,0])
w2 = list2vec([0,0,1])

v0 = list2vec([1,2,3])
v1 = list2vec([1,3,3])
v2 = list2vec([0,3,3])

# Fill in exchange_S1 and exchange_S2
# with appropriate lists of 3 vectors

exchange_S0 = [w0, w1, w2]
exchange_S1 = [v0, w1, w2]
exchange_S2 = [v0, v1, w2]
exchange_S3 = [v0, v1, v2]



## 2: (Problem 6.7.3) Another Iterative Exchange Lemma
w0 = list2vec([0,one,0])
w1 = list2vec([0,0,one])
w2 = list2vec([one,one,one])

v0 = list2vec([one,0,one])
v1 = list2vec([one,0,0])
v2 = list2vec([one,one,0])

exchange_2_S0 = [w0, w1, w2]
exchange_2_S1 = [w0, w2, v2]
exchange_2_S2 = [v0, w2, v2]
exchange_2_S3 = [v0, v1, v2]

## 3: (Problem 6.7.4) Morph Lemma Coding
def morph(S, B):
    '''
    Input:
        - S: a list of distinct Vecs
        - B: a list of linearly independent Vecs all in Span S
    Output: a list of pairs of vectors to inject and eject (see problem description)
    Example:
        >>> # This is how our morph works.  Yours may yield different results.
        >>> # Note: Make a copy of S to modify instead of modifying S itself.
        >>> from vecutil import list2vec
        >>> from vec import Vec
        >>> S = [list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
        >>> B = [list2vec(v) for v in [[1,1,0],[0,1,1],[1,0,1]]]
        >>> D = {0, 1, 2}
        >>> morph(S, B) == [(Vec(D,{0: 1, 1: 1, 2: 0}), Vec(D,{0: 1, 1: 0, 2: 0})), (Vec(D,{0: 0, 1: 1, 2: 1}), Vec(D,{0: 0, 1: 1, 2: 0})), (Vec(D,{0: 1, 1: 0, 2: 1}), Vec(D,{0: 0, 1: 0, 2: 1}))]
        True
        >>> S == [list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
        True
        >>> B == [list2vec(v) for v in [[1,1,0],[0,1,1],[1,0,1]]]
        True
        >>> from GF2 import one
        >>> D = {0, 1, 2, 3, 4, 5, 6, 7}
        >>> S = [Vec(D,{1: one, 2: one, 3: one, 4: one}), Vec(D,{1: one, 3: one}), Vec(D,{0: one, 1: one, 3: one, 5: one, 6: one}), Vec(D,{3: one, 4: one}), Vec(D,{3: one, 5: one, 6: one})]
        >>> B = [Vec(D,{2: one, 4: one}), Vec(D,{0: one, 1: one, 2: one, 3: one, 4: one, 5: one, 6: one}), Vec(D,{0: one, 1: one, 2: one, 5: one, 6: one})]
        >>> sol = morph(S, B)
        >>> sol == [(B[0],S[0]), (B[1],S[2]), (B[2],S[3])] or sol == [(B[0],S[1]), (B[1],S[2]), (B[2],S[3])]
        True
        >>> # Should work the same regardless of order of S
        >>> from random import random
        >>> sol = morph(sorted(S, key=lambda x:random()), B)
        >>> sol == [(B[0],S[0]), (B[1],S[2]), (B[2],S[3])] or sol == [(B[0],S[1]), (B[1],S[2]), (B[2],S[3])]
        True
    '''
    from matrix.The_Basis_problems import exchange
    injections = []
    ejections = []
    S_copy = S.copy()
    for v in B:
        injections.append(v)
        ejections.append(exchange(S_copy, ejections, v))
        S_copy.remove(ejections[-1])
        S_copy.append(v)

    return [(i, e) for i, e in zip(injections, ejections)]


## 4: (Problem 6.7.5) Row and Column Rank Practice
# Please express each solution as a list of Vecs

row_space_1 = [list2vec([1, 2, 0]), list2vec([0, 2, 1])]
col_space_1 = [list2vec([1, 0]), list2vec([0, 1])]

row_space_2 = [list2vec([1, 4, 0, 0]), list2vec([0, 2, 2, 0]), list2vec([0, 0, 1, 1])]
col_space_2 = [list2vec([1, 0, 0]), list2vec([0, 2, 1]), list2vec([0, 0, 1])]

row_space_3 = [list2vec([1])]
col_space_3 = [list2vec([1, 2, 3])]

row_space_4 = [list2vec([1, 0]), list2vec([2, 1])]
col_space_4 = [list2vec([1, 2, 3]), list2vec([0, 1, 4])]



## 5: (Problem 6.7.6) My Is Independent Procedure
def my_is_independent(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - boolean: true if the list is linearly independent
    Examples:
        >>> D = {0, 1, 2}
        >>> L = [Vec(D,{0: 1}), Vec(D,{1: 1}), Vec(D,{2: 1}), Vec(D,{0: 1, 1: 1, 2: 1}), Vec(D,{0: 1, 1: 1}), Vec(D,{1: 1, 2: 1})]
        >>> my_is_independent(L)
        False
        >>> my_is_independent(L[:2])
        True
        >>> my_is_independent(L[:3])
        True
        >>> my_is_independent(L[1:4])
        True
        >>> my_is_independent(L[0:4])
        False
        >>> my_is_independent(L[2:])
        False
        >>> my_is_independent(L[2:5])
        False
        >>> L == [Vec(D,{0: 1}), Vec(D,{1: 1}), Vec(D,{2: 1}), Vec(D,{0: 1, 1: 1, 2: 1}), Vec(D,{0: 1, 1: 1}), Vec(D,{1: 1, 2: 1})]
        True
    '''
    return rank(L) == len(L)



## 6: (Problem 6.7.7) My Rank
def my_rank(L):
    '''
    Input: 
        - L: a list of Vecs
    Output: 
        - the rank of the list of Vecs
    Example:
        >>> L = [list2vec(v) for v in [[1,2,3],[4,5,6],[1.1,1.1,1.1]]]
        >>> my_rank(L)
        2
        >>> L == [list2vec(v) for v in [[1,2,3],[4,5,6],[1.1,1.1,1.1]]]
        True
        >>> my_rank([list2vec(v) for v in [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[123,432,123]]])
        2
    '''
    from matrix.The_Basis_problems import subset_basis
    return len(subset_basis(L))



## 7: (Problem 6.7.9) Direct Sum Validity
# Please give each answer as a boolean

only_share_the_zero_vector_1 = True
only_share_the_zero_vector_2 = True
only_share_the_zero_vector_3 = True



## 8: (Problem 6.7.11) Direct Sum Unique Representation
def direct_sum_decompose(U_basis, V_basis, w):
    '''
    Input:
        - U_basis: a list of Vecs forming a basis for a vector space U
        - V_basis: a list of Vecs forming a basis for a vector space V
        - w: a Vec in the direct sum of U and V
    Output:
        - a pair (u, v) such that u + v = w, u is in U, v is in V
    Example:

        >>> D = {0,1,2,3,4,5}
        >>> U_basis = [Vec(D,{0: 2, 1: 1, 2: 0, 3: 0, 4: 6, 5: 0}), Vec(D,{0: 11, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0}), Vec(D,{0: 3, 1: 1.5, 2: 0, 3: 0, 4: 7.5, 5: 0})]
        >>> V_basis = [Vec(D,{0: 0, 1: 0, 2: 7, 3: 0, 4: 0, 5: 1}), Vec(D,{0: 0, 1: 0, 2: 15, 3: 0, 4: 0, 5: 2})]
        >>> w = Vec(D,{0: 2, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0})
        >>> (u, v) = direct_sum_decompose(U_basis, V_basis, w)
        >>> (u + v - w).is_almost_zero()
        True
        >>> U_matrix = coldict2mat(U_basis)
        >>> V_matrix = coldict2mat(V_basis)
        >>> (u - U_matrix*solve(U_matrix, u)).is_almost_zero()
        True
        >>> (v - V_matrix*solve(V_matrix, v)).is_almost_zero()
        True
        >>> ww = Vec(D,{0: 2, 1: 5, 2: 51, 4: 1, 5: 7})
        >>> (u, v) = direct_sum_decompose(U_basis, V_basis, ww)
        >>> (u + v - ww).is_almost_zero()
        True
        >>> (u - U_matfrrix*solve(U_matrix, u)).is_almost_zero()
        True
        >>> (v - V_matrix*solve(V_matrix, v)).is_almost_zero()
        True
        >>> U_basis == [Vec(D,{0: 2, 1: 1, 2: 0, 3: 0, 4: 6, 5: 0}), Vec(D,{0: 11, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0}), Vec(D,{0: 3, 1: 1.5, 2: 0, 3: 0, 4: 7.5, 5: 0})]
        True
        >>> V_basis == [Vec(D,{0: 0, 1: 0, 2: 7, 3: 0, 4: 0, 5: 1}), Vec(D,{0: 0, 1: 0, 2: 15, 3: 0, 4: 0, 5: 2})]
        True
        >>> w == Vec(D,{0: 2, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0})
        True
    '''
    U_V_matrix = coldict2mat(U_basis + V_basis)
    # print(U_V_matrix)
    result = solve(U_V_matrix, w)
    scalars = [result[d] for d in result.D]
    u = sum([s*v for s, v in zip(scalars[:len(U_basis)], U_basis)])
    v = sum([s*v for s, v in zip(scalars[len(U_basis):], V_basis)])
    return (u, v)



## 9: (Problem 6.7.12) Is Invertible Function
def is_invertible(M):
    '''
    6.4.7 Matrix Invertibility
    Let M be an R × C matrix. Then M is invertible if and only if |R| = |C| and the columns of M are linearly independent.
    :param M: A matrix, M
    :return: A boolean indicating if M is invertible.

    >>> M = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 1, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 1, (2, 0): 0, (1, 3): 0, (2, 3): 1, (2, 2): 3, (1, 0): 0, (0, 3): 0})
    >>> is_invertible(M)
    True

    >>> M1 = Mat(({0,1,2},{0,1,2}),{(0,0):1,(0,2):2,(1,2):3,(2,2):4})
    >>> is_invertible(M1)
    False

    >>> M0_GF2 = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 0): one, (0, 2): one, (1, 1): one, (1, 2): one, (2, 0): one, (2, 1): one})
    >>> is_invertible(M0_GF2)
    False

    >>> M1_GF2 = Mat(({0, 1}, {0, 1}), {(0, 0): one, (0, 1): one, (1, 1): one})
    >>> is_invertible(M1_GF2)
    True

    '''
    cols = list(mat2coldict(M).values())
    rows = list(mat2rowdict(M).values())
    # print(rank(rows), rows)
    # print(rank(cols), cols)
    # print(is_independent(cols))
    # TODO: determine why linear independence of the rows matters, which is not what is called out in 6.4.7 Matrix Invertibility
    return rank(cols) == rank(rows) and is_independent(cols) and is_independent(rows)



## 10: (Problem 6.7.13) Inverse of a Matrix over GF(2)
def find_matrix_inverse(A):
    '''
    Input:
        - A: an invertible Mat over GF(2)
    Output:
        - A Mat that is the inverse of A
    Examples:
        >>> M1 = Mat(({0,1,2}, {0,1,2}), {(0, 1): one, (1, 0): one, (2, 2): one})
        >>> find_matrix_inverse(M1) == Mat(M1.D, {(0, 1): one, (1, 0): one, (2, 2): one})
        True
        >>> find_matrix_inverse(M1) * M1 == identity(M1.D[0], one)
        True
        >>> M1 * find_matrix_inverse(M1) == identity(M1.D[0], one)
        True
    '''
    # print(coldict2mat([solve(A, idm_col) for idm_col in mat2coldict(identity(A.D, one)).values()]))
    # print(identity(A.D[0], one))
    # return identity(A.D[0], one)
    return coldict2mat([solve(A, idm_col) for idm_col in mat2coldict(identity(A.D[0], one)).values()])


## 11: (Problem 6.7.14) Inverse of a Triangular Matrix
def find_triangular_matrix_inverse(A):
    '''
    Supporting GF2 is not required.

    Input:
        - A: an upper triangular Mat with nonzero diagonal elements
    Output:
        - Mat that is the inverse of A
    
    Example:
        >>> A = listlist2mat([[1, .5, .2, 4],[0, 1, .3, .9],[0,0,1,.1],[0,0,0,1]])
        >>> find_triangular_matrix_inverse(A) == Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): -0.5, (1, 2): -0.3, (3, 2): 0.0, (0, 0): 1.0, (3, 3): 1.0, (3, 0): 0.0, (3, 1): 0.0, (2, 1): 0.0, (0, 2): -0.05000000000000002, (2, 0): 0.0, (1, 3): -0.87, (2, 3): -0.1, (2, 2): 1.0, (1, 0): 0.0, (0, 3): -3.545, (1, 1): 1.0})
        True
    '''
    return coldict2mat([triangular_solve(list(mat2rowdict(A).values()), list(A.D[0]), idm_col) for idm_col in mat2coldict(identity(A.D[0], 1)).values()])

