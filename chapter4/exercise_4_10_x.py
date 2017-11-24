from matutil import listlist2mat
from vecutil import list2vec
from chapter4.example_4_9_x import example_4_9_3, example_4_9_4, example_4_9_5, example_4_9_6
from itertools import combinations_with_replacement

# Linear Function Properties
# L1: f(a * u) == a * f(u)
# L2: f(u + v) == f(u) + f(v)

a = 2
u = list2vec([1, 0])
v = list2vec([0, 1])


def exercise_4_10_7(v):
    """
    The doctest below demonstrates the function is not because it violates L1 and L2 above.
    :param v: 2-vector x, y
    :return: 3-vector x, y, 1

    >>> L = exercise_4_10_7(a * u)
    >>> L == list2vec([2, 0, 1])
    True
    >>> R = a * exercise_4_10_7(u)
    >>> R == list2vec([2, 0, 2])
    True
    >>> L == R
    False
    >>> L = exercise_4_10_7(u + v)
    >>> L == list2vec([1, 1, 1])
    True
    >>> R = exercise_4_10_7(u) + exercise_4_10_7(v)
    >>> R == list2vec([1, 1, 2])
    True
    >>> L == R
    False
    """
    return list2vec([v[0], v[1], 1])


def exercise_4_10_8(v):
    """
    Take a point and reflect about the y-axis (e.g. (x, y) -> (-x, y)
    This is a linear function because it satisfies properties L1 and L2 above.
    :param v: 2-vector x, y
    :return: v translated about the y-axis

    >>> L = exercise_4_10_8(a * u)
    >>> L == list2vec([-2, 0])
    True
    >>> R = a * exercise_4_10_8(u)
    >>> R == list2vec([-2, 0])
    True
    >>> L == R
    True

    >>> L = exercise_4_10_8(u + v)
    >>> L == list2vec([-1, 1])
    True
    >>> R = exercise_4_10_8(u) + exercise_4_10_8(v)
    >>> R == list2vec([-1, 1])
    True
    >>> L == R
    True
    """
    return v * listlist2mat([[-1, 0], [0, 1]])


# Problem 4.10.9
# TODO: According to the book at least one function in 4.9.x is not linear. I cannot figure out how to prove it
def is_func_linear(f):
    """
    Evaluate function f to determine if it is linear by the properties L1 and L2

    :param f: a function accepting a vector
    :return: boolean indicating if f is a linear function

    >>> funcs = [example_4_9_3, example_4_9_4, example_4_9_5, example_4_9_6]
    >>> {f.__name__ for f in funcs if not is_func_linear(f)}
    set()
    """
    is_linear = True
    scalars = range(-1, 2)
    combos = list(combinations_with_replacement([p for p in combinations_with_replacement(range(-1, 2), 2)], 2))
    for a in scalars:
        for combo in combos:
            print(a)
            u = list2vec(combo[0])
            v = list2vec(combo[1])
            residual_l = f(a * u) - a * f(u)
            residual_r = f(u + v) - (f(u) + f(v))
            if residual_l*residual_l > .1 or residual_l*residual_l < -.1 or residual_r*residual_r > .1 or residual_r*residual_r < -.1:
                is_linear = False
                print(f.__name__, a, repr(u), repr(v))
                print(repr(f(a * u)), repr(a * f(u)), repr(f(u + v)), repr(f(u) + f(v)))

    # print(f.__name__, a, repr(u), repr(v))
    # print(repr(f(a * u)), repr(a * f(u)), repr(f(u + v)), repr(f(u) + f(v)))
    # return f(a * u) == a * f(u) and f(u + v) == f(u) + f(v)
    return is_linear
