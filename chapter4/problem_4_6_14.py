from matutil import listlist2mat
from vecutil import list2vec

def prove_equation_4_4(M, u, v):
    """
    :param M: R x C matrix
    :param u: C-vector
    :param v: C-vector
    :return: boolean to validate if the proposition below is true

    >>> M = listlist2mat([[4, 5, 6],[7, 8, 9]])
    >>> u = list2vec([1, 2, 3])
    >>> v = list2vec([0, -1, -2])
    >>> prove_equation_4_4(M, u, v)
    True
    """
    return M * (u + v) == M * u + M * v