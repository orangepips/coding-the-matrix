from resources.vecutil import list2vec
from resources.matutil import rowdict2mat, mat2rowdict, listlist2mat
from resources.mat import Mat
from resources.independence import rank
from resources.vec import Vec


# ||v|| == sqrt(<v, v>)
# <v, v> == v * v

# Problem 8.3.4
def lemma_8_3_3(a, u, b, v):
    """
    Demonstrates that if u is orthogonal to v then for any scalars a, b it continues to be true
    :param a: scalar
    :param u: n vector
    :param b: scalar
    :param v: n vector
    :return: a^2 * ||u||^2 + b^2 * ||v||^2
    >>> u = list2vec([1, 0])
    >>> v = list2vec([0, 1])
    >>> a = 2
    >>> b = 3
    >>> result = lemma_8_3_3(a, u, b, v)
    >>> result[0] == result[1]
    True
    >>> u = list2vec([1, 1]) # not orthogonal
    >>> v = list2vec([0, 1])
    >>> a = 2
    >>> b = 3
    >>> result = lemma_8_3_3(a, u, b, v)
    >>> result[0] != result[1]
    True
    """
    # t1 = (a * u + b * v) * (a * u + b * v)
    t1 = sum([(a*u), (b*v)])
    t1 *= t1
    t2 = a**2 * ((u * u)**(1/2))**2 + b**2 * ((v * v)**(1/2))**2
    return t1, t2


# Problem 8.3.5
def lemma_8_3_3_generalized(scalars, vectors):
    """
    Demonstrates that if v1... vn are mutually orthogonal that for any coefficients a1.... an
    ||a1 * v1 + ... + an * vn||^2 == a1^2 * ||v1||^2 + ... + an^2 * ||vn||^2
    :param scalars: n length list of scalars
    :param vectors: n length list of m vectors
    :return: 2-tuple with each side of description equation
    >>> scalars = [2, 3]
    >>> vectors = [list2vec([1, 0]), list2vec([0, 1])]
    >>> result = lemma_8_3_3_generalized(scalars, vectors)
    >>> result[0] == result[1]
    True
    >>> scalars2 = [2, 3]
    >>> vectors2 = [list2vec([1, 1]), list2vec([0, 1])] # not orthogonal
    >>> result = lemma_8_3_3_generalized(scalars2, vectors2)
    >>> result[0] != result[1]
    True
    >>> scalars3 = [2, 3, 4]
    >>> vectors3 = [list2vec([1, 0, 0]), list2vec([0, 1, 0]), list2vec([0, 0, 1])]
    >>> result = lemma_8_3_3_generalized(scalars3, vectors3)
    >>> result[0] == result[1]
    True
    >>> scalars4 = [2, 3, 4]
    >>> vectors4 = [list2vec([1, 0, 1]), list2vec([0, 1, 0]), list2vec([0, 0, 1])] # not orthogonal
    >>> result = lemma_8_3_3_generalized(scalars4, vectors4)
    >>> result[0] != result[1]
    True
    """
    t1 = sum([(s * v) for s, v in zip(scalars, vectors)])
    t1 *= t1 # because the Vec clas does not have the 'pow' operator implemented
    t2 = sum([s**2 * ((v*v)**(1/2))**2 for s, v in zip(scalars, vectors)])
    return t1, t2


# πᵥ(x) == projection of x along v
# πᵥ(x) == (v * x)v
# Problem 8.3.15 & 8.3.16
def projection_matrix(v):
    """
    Given vector v returns matrix M such that πᵥ(x) == Mx
    :param v: vector
    :return: matrix
    >>> v = list2vec([2, 0, 2])
    >>> result = projection_matrix(v)
    >>> result == Mat(({0}, {0}), {(0, 0): 8})
    True
    >>> rank(list(mat2rowdict(result).values()))
    1
    """
    return rowdict2mat([v]) * rowdict2mat([v]).transpose()


# 8.3.17 > 1 & 2
def scalar_mul_count_M_v(M, v):
    """
    Multiply M * v and return count of scalar multiplications involved
    :param M: n x m matrix (n - rows, m - cols)
    :param v: m vector
    :return: scalar multiplication count == n * m (#1)
    >>> M = listlist2mat([[1, 2, 3], [4, 5, 6]])
    >>> v = list2vec([1, 1, 1])
    >>> scalar_mul_count_M_v(M, v) == len(M.D[0]) * len(v.D)
    True
    >>> M1 = listlist2mat([[1], [1], [1]])
    >>> M2 = listlist2mat([[1, 1, 1]])
    >>> x = list2vec([1, 1, 1])
    >>> scalar_mul_count_M_v(M2, x) + scalar_mul_count_M_v(M1, M2 * x) == 2 * len(x.D) # == M1 * (M2x)
    True
    """

    class MatInnerProduct(Mat):
        scalar_scalar_mul_count = 0

        def __mul__(M, v):
            assert M.D[1] == v.D
            r = Vec(M.D[0], {})
            for i in M.D[0]:
                for j in M.D[1]:
                    M.scalar_scalar_mul_count += 1
                    if M[i, j] == 0: continue
                    r[i] = r[i] + M[i, j] * v[j]
            return r

    MIP = MatInnerProduct(M.D, M.f)
    MIP * v
    return MIP.scalar_scalar_mul_count