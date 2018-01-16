from resources.mat import Mat
from resources.vec import Vec
from math import sqrt

# Problem 10.11.1
def orthogonal_vec2rep(Q, b):
    """
    :param Q: an orthogonal matrix
    :param b: vector whose label set equals the column-label set of Q
    :return: coordinate representation of b in terms of the rows of Q
    >>> Q = Mat(({'A', 'B', 'C'}, {1, 2, 3}), { \
        ('A', 1): 1/sqrt(2), ('A', 2): 1/sqrt(2), ('A', 3): 0, \
        ('B', 1): 1/sqrt(3), ('B', 2): -1/sqrt(3), ('B', 3): 1/sqrt(3), \
        ('C', 1): -1/sqrt(6), ('C', 2): 1/sqrt(6), ('C', 3): 2/sqrt(6) \
    })
    >>> b = Vec(Q.D[1], {1: 10, 2: 20, 3: 30})
    >>> expected = Vec(Q.D[0], {"A": 21.213, "B": 11.547, "C": 28.577})
    >>> actual = orthogonal_vec2rep(Q, b)
    >>> (actual - expected) * (actual - expected) < 1e-5
    True
    """
    return Q * b


# Problem 10.11.2
def orthogonal_change_of_basis(A, B, a):
    """
    :param A: orthogonal matrix with row-label set == column-label set
    :param B: orthogonal matrix same row and column labels as A
    :param a: vector coordinate representation in terms of the rows of A
    :return: coordinate representation v in terms of the columns of B
    >>> A = Mat(({1, 2, 3}, {1, 2, 3}), { \
        (1, 1): 1/sqrt(2), (1, 2): 1/sqrt(2), (1, 3): 0, \
        (2, 1): 1/sqrt(3), (2, 2): -1/sqrt(3), (2, 3): 1/sqrt(3), \
        (3, 1): -1/sqrt(6), (3, 2): 1/sqrt(6), (3, 3): 2/sqrt(6) \
    })
    >>> B = A.copy()
    >>> a = Vec(A.D[0], {1: sqrt(2), 2: 1/sqrt(3), 3:2/sqrt(6)})
    >>> expected = Vec(B.D[1], {1: .876, 2: .538, 3: 1.393})
    >>> actual = orthogonal_change_of_basis(A, B, a)
    >>> (actual - expected) * (actual - expected) < 1e-5
    True
    """
    return a*B*A


# Problem 10.11.3
# https://github.com/kjy/LinearAlgebra_python/blob/master/hw7.py#L121
def orthonormal_projection_orthogonal(W, b):
    """
    :param W: matrix whose rows are orthonormal
    :param b: vector whose label set is the column-label set of W
    :return: projection of b orthogonal to the row space of W
    >>> W = Mat(({'A', 'B'}, {1, 2, 3}), { \
        ('A', 1): 1/sqrt(2), ('A', 2): 1/sqrt(2), ('A', 3): 0, \
        ('B', 1): 1/sqrt(3), ('B', 2): -1/sqrt(3), ('B', 3): 1/sqrt(3) \
    })
    >>> b = Vec(W.D[1], {1: 10, 2: 20, 3: 30})
    >>> expected = Vec(W.D[1], {1: -11 - 2/3, 2: 11 + 2/3, 3: 23 + 1/3})
    >>> actual = orthonormal_projection_orthogonal(W, b)
    >>> (actual - expected) * (actual - expected) < 1e-5
    True
    """
    from resources.orthogonalization import project_orthogonal
    from resources.matutil import mat2rowdict
    return project_orthogonal(b, list(mat2rowdict(W).values()))
