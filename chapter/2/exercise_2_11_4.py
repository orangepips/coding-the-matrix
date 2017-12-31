from chapter2.vecutil import list2vec, zero_vec

"""
2.10.2 does not make clear you must implement all shell methods listed in 
vec.py for the Vec class. Familiarize yourself with doctest to understand how 
to do this properly as the book neglects to explain. 

Turns out problem 2.14.10 covers doctest. Seems out of order. 

https://docs.python.org/3/library/doctest.html 

PyCharm has good doctest support. 
"""

def triangular_solve_n(rowlist, b):
    """
    :param rowlist: triangular system of n-vectors
    :param b: list of numbers length-n
    :return: vector solve for triangular equation

    >>> rowlist = [list2vec([1, -3, -2]), list2vec([0, 2, 4]), list2vec([0, 0, -10])]
    >>> b = [7, 4, 12]
    >>> triangular_solve_n(rowlist, b)
    Vec({0, 1, 2},{0: 17.8, 1: 4.4, 2: -1.2})
    """
    D = rowlist[0].D
    n = len(D)
    assert D == set(range(n))
    x = zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
    return x


