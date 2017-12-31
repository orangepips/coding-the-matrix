from grading.factoring_support import intsqrt, gcd, dumb_factor, primes, prod
from grading.echelon import transformation_rows
from random import randint
from resources.GF2 import one
from resources.vec import Vec
from operator import mul
from functools import reduce

# Task 7.8.1
def root_method(N):
    '''
    Find b for a^2 - b^2 = N
    :param N: integer
    :return: b
    >>> root_method(55)
    5
    >>> root_method(77)
    1
    >>> root_method(146771)
    317
    >>> root_method(118) # None
    '''
    a = intsqrt(N) + 1
    while True:
        b = intsqrt(a**2 - N)
        # print(a, b)
        if b**2 == a**2 - N:
            return a - b
        elif a >= N:
            return None
        else:
            a += 1


# 7.8.2
def euclids_algorithm(r, s, t):
    '''
    Evaluate three integers to find the greatest divisor of a = r*s and b = s*t
    :param r: integer
    :param s: integer
    :param t: integer
    :return: greatest divisor
    >>> r = randint(1000, 100000)
    >>> s = randint(1000, 100000)
    >>> t = randint(1000, 100000)
    >>> euclids_algorithm(r, s, t)
    True
    '''
    a = r * s
    b = s * t
    d = gcd(a, b)
    assert a%d == 0
    assert b%d == 0
    assert d >= s
    return True


# 7.8.3
def a_b_gcd():
    '''
    :return: gcd of a and b
    >>> a_b_gcd()
    44
    '''
    N = 367160330145890434494322103
    a = 67469780066325164
    b = 9429601150488992
    assert (a * a - b * b) % N == 0
    return gcd(a, b)

# 7.8.4
def dumb_factor_primeset(x):
    '''
    >>> dumb_factor_primeset(12)
    [(2, 2), (3, 1)]
    >>> dumb_factor_primeset(154)
    [(2, 1), (7, 1), (11, 1)]
    >>> dumb_factor_primeset(2 * 3 * 3 * 3 * 11 * 11)
    [(2, 1), (3, 3), (11, 2)]
    >>> dumb_factor_primeset(2 * 17)
    []
    >>> dumb_factor_primeset(2 * 3 * 5 * 7 * 19)
    []
    '''
    primeset = {2, 3, 5, 7, 11, 13}
    return dumb_factor(x, primeset)


# 7.8.5
def int2GF2(i):
    '''
    Return GF2 indicator of even or oddness for i
    :param i: an integer
    :return: one if odd, 0 if even
    >>> int2GF2(3)
    one
    >>> int2GF2(4)
    0
    '''
    return 0 if i % 2 == 0 else one


# 7.8.6
def make_Vec(primeset, factors):
    '''
    :param primeset: set of primes
    :param factors: list of tuples [(p1, a1)... (pn, an)] where every pi belongs to primeset
    :return: primeset vector over GF2 with domain primeset such that v[pi] = int2GF(ai) for i=1... s
    >>> make_Vec({2,3,5,7,11}, [(3,1)]) == Vec({2,3,5,7,11}, {3: one})
    True
    >>> make_Vec({2,3,5,7,11}, [(2,17), (3, 0), (5,1), (11,3)]) == Vec({2,3,5,7,11}, {2: one, 3: 0, 5: one, 11: one})
    True
    '''
    return Vec(primeset, {t[0]:int2GF2(t[1]) for t in factors})


# 7.8.7
N = 2419
def find_candidiates(N, primeset):
    '''
    finds len(primeset) + 1 integers a for which a * a - N can be factored over primeset
    :param N: integer to be factored
    :param primeset: set of primes
    :return: two lists:
        (1) roots: a1, a2, a3... aN such that ai * ai - N can be factored completely over primeset and
        (2) rowlist: element i is the primeset vector over GF(2) corresponding to ai (same as
        make_Vec(primeset, factors) result)
    >>> primeset = primes(32)
    >>> roots, rowlist = find_candidiates(N, primeset)
    >>> roots == [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]
    True
    >>> rowlist[0] == Vec(primeset, {2: one, 7: one, 13: one})
    True
    >>> rowlist[-1] == Vec(primeset, {2: one, 3: one, 7: 0, 13: one})
    True
    '''
    roots = []
    rowlist = []

    y = 2
    while True:
        x = intsqrt(N) + y
        delta = x * x - N
        factors = dumb_factor(delta, primeset)
        # print(x, delta, factors, reduce(mul, [r**e for r,e in factors], 1))
        if delta == reduce(mul, [r**e for r,e in factors], 1):
            roots.append(x)
            rowlist.append(make_Vec(primeset, factors))
        if len(roots) >= len(primeset) + 1:
            break
        y += 1

    return roots, rowlist


# 7.8.8 & 7.8.9
def gcd_candidate(p, q, M):
    '''
    :param p:
    :param q:
    :param M:
    :return:
    >>> a1 = 53 * 77
    >>> b1 = 2 * 3**2 * 5 * 13
    >>> candidate1 = gcd_candidate(a1, b1, N)
    >>> candidate1 == 41
    True
    >>> N % candidate1
    0
    >>> a2 = 52 * 67 * 71
    >>> b2 = 2 * 3**2 * 5 * 19 * 23
    >>> candidate2 = gcd_candidate(a2, b2, N)
    >>> candidate2 == 2419
    True
    >>> N % candidate2
    0
    '''
    return gcd(p - q, M)


# 7.8.10
def find_a_and_b(v, roots, N):
    '''
    Determine pair of integers N % a**2 - b**2 == 0
    :param v: vector, one of the rows of M
    :param roots: list
    :param N: integer to factor
    :return: pair of integers (a, b)
    >>> primeset = primes(32)
    >>> roots, rowlist = find_candidiates(N, primeset)
    >>> M = transformation_rows(rowlist)
    >>> v = M[-1]
    >>> a, b = find_a_and_b(v, roots, N)
    >>> gcd(a - b, N)
    1
    >>> v = M[-2]
    >>> a, b = find_a_and_b(v, roots, N)
    >>> gcd(a - b, N)
    41
    '''
    alist = [roots[d] for d in v.D if v[d] == one]
    # print(v.f, roots, N, alist)
    a = prod(alist)
    c = prod([e * e - N for e in alist])
    b = intsqrt(c)
    assert b * b == c
    return a, b


# 7.8.11-13
def find_first_x_divisors(n, primeset, x=1):
    """
    Find divisors of n
    :param n: integer to factor
    :param primeset: set of prime numbers
    :param x: max number of divisors to find
    :return: list of divisors
    >>> find_first_x_divisors(N, primes(32), 2)
    {41, 59}
    >>> find_first_x_divisors(2461799993978700679, primes(10000))
    {1230926561}
    >>> find_first_x_divisors(20672783502493917028427, primes(10000))
    {1230926561}

    # last test takes 10 minutes
    """
    roots, rowlist = find_candidiates(n, primeset)
    # supposedly this reverse order creates a speedup b/c a large prime is less likely to be a divisor
    # in practice, not noticing a difference, but haven't timed
    M_rows = transformation_rows(rowlist, sorted(list(primeset), reverse=True)) # 7.8.13
    result = set()
    for row in reversed(M_rows):
        try:
            a, b = find_a_and_b(row, roots, n)
        except AssertionError:
            break
        divisor = gcd(a - b, n)
        if divisor != 1 and divisor != n:
            result.add(divisor)
        if len(result) >= x:
            break
    return result
