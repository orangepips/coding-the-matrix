import logging

from resources.vecutil import list2vec
from chapter4.example_4_9_x import example_4_9_3, example_4_9_4, example_4_9_5, example_4_9_6
from itertools import combinations_with_replacement

# Linear Function Properties
# L1: f(a * u) == a * f(u)
# L2: f(u + v) == f(u) + f(v)

a = 2
u = list2vec([1, 0])
v = list2vec([0, 1])


def example_4_10_4(v):
    """
    Lemma 4.10.3: For any C-vector a over F, the function f: FC −→ F defined by f(x) = a·x is a linear function.

    Bilinearity of dot-product Lemma 4.10.3 states that, for any vector w, the function x → w · x is a linear function
    of x. Thus the dot-product function f(x, y) = x · y is linear in its first argument (i.e. if we plug in a vector for
    the second argument). By the symmetry of the dot-product (Proposition 2.9.21), the dot-product function is also
    linear in its second argument. We say that the dot-product function is bilinear to mean that it is linear in each of
    its arguments.

    Let F be any field. The function from F2 to F defined by (x, y) → x + y is a linear function. You can prove this
    using bilinearity of dot-product.
    :param v: 2-vector x,y
    :return: x + y

    >>> L1 = example_4_10_4(a * u)
    >>> R1 = a * example_4_10_4(u)
    >>> L1 == R1
    True

    >>> L2 = example_4_10_4(u + v)
    >>> R2 = example_4_10_4(u) + example_4_10_4(v)
    >>> L2 == R2
    True
    """
    return v[0] + v[1]

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
    return list2vec([-v[0], v[1]])


# Problem 4.10.9
def is_func_linear(f):
    """
    Evaluate function f to determine if it is linear by the properties L1 and L2

    :param f: a function accepting a vector
    :return: boolean indicating if f is a linear function

    >>> funcs = [example_4_9_3, example_4_9_4, example_4_9_5, example_4_9_6]
    >>> {f.__name__ for f in funcs if not is_func_linear(f)}
    {'example_4_9_6'}
    """
    logger = logging.getLogger()
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    is_linear = True
    scalars = range(-1, 2)
    combos = list(combinations_with_replacement([p for p in combinations_with_replacement(range(-1, 2), 2)], 2))
    for a in scalars:
        for combo in combos:
            # print(a)
            u = list2vec(combo[0])
            v = list2vec(combo[1])
            residual_l = f(a * u) - a * f(u)
            residual_r = f(u + v) - (f(u) + f(v))
            if residual_l*residual_l > .1 or residual_l*residual_l < -.1 or residual_r*residual_r > .1 or residual_r*residual_r < -.1:
                is_linear = False
                logger.debug("Function: {0}\ta: {1}\tu: {2}\tv: {3}".format(f.__name__, a, repr(u), repr(v)))
                logger.debug("\tf(a * u):\t{0}".format(repr(f(a * u))))
                logger.debug("\ta * f(u):\t{0}".format(repr(a * f(u))))
                logger.debug("\tf(u + v):\t{0}".format(repr(f(u + v))))
                logger.debug("\tf(u) + f(v):{0}".format(repr(f(u) + f(v))))

    return is_linear
