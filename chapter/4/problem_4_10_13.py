from resources.vecutil import list2vec


def kernel(v):
    """
    Analogous to the null space of a matrix (Definition 4.7.1), we define the kernel of a linear function f to be
    {v: f(v) = 0}. We denote the kernel of f by Ker f.

    :param v: 2-vector x,y

    Prove Lemma 4.10.12 by showing that Ker f satisfies Properties V1, V2, and V3 of vector spaces (Section 3.4).
    V is the span of some D-vectors over F or the solution set of a linear system, has three properties:
    Property V1: V contains the zero vector,
    Property V2: For every vector v, if V contains v then it contains α v for every scalar α, is closed under
      scalar-vector multiplication, and
    Property V3: For every pair u and v of vectors, if V contains u and v then it contains u + v.

    :return: zero vector in v's domain

    >>> a = 2
    >>> v = list2vec([1,2])
    >>> actual1 = kernel(v)
    >>> expected1 = list2vec([-1, -2])
    >>> actual1 == expected1
    True
    >>> actual2 = kernel(a * v)
    >>> expected2 = list2vec([-2, -4])
    >>> actual2 == expected2
    True
    >>> u = a * v
    >>> actual3 = kernel(u + v)
    >>> expected3 = list2vec([-3, -6])
    >>> actual3 == expected3
    True
    """
    return list2vec([-v[0], -v[1]])

