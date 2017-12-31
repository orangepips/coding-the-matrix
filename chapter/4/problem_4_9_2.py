from resources.mat import Mat
from resources.vec import Vec

# Example 4.9.1 & Problem 4.9.2
def evaluate_zero_vector(M, i):
    """
    :param M: R x C matrix
    :param i: C-vector (a.k.a. image)
    :return: M * i an R-vector
    >>> M = Mat(\
        ({'a','b'}, {'#', '@', '?'}),\
        {\
            ('a', '#'): 1, ('a', '@'): 2, ('a', '?'): 3,\
            ('b', '#'): 10, ('b', '@'): 20, ('b', '?'): 30\
        }\
    )
    >>> i = Vec({'#', '@', '?'}, {'#': 2, '@': 2, '?': -2})
    >>> evaluate_zero_vector(M, i) == Vec({'a', 'b'}, {'a': 0, 'b': 0})
    True
    >>> Mt = M.transpose()
    >>> it = Vec({'a', 'b'}, {'a': 10, 'b': -1})
    >>> evaluate_zero_vector(Mt, it) == Vec({'#', '@', '?'}, {'#': 0, '@': 0, '?': 0})
    True
    """
    return M * i