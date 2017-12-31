# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

import random
from resources.GF2 import one
from resources.vecutil import list2vec
from resources.independence import is_independent
from itertools import combinations, chain


## 1: (Task 7.7.1) Choosing a Secret Vector
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    '''
    Generate a random vector whose linear combination with a0 and b0 is equal to the passed
    scalars s and t.
    :param s: GF2 scalar
    :param t: GF2 scalar
    :return: vector u such that a0*u==s and b0*u==t
    >>> s=one
    >>> t=0
    >>> u=choose_secret_vector(s, t)
    >>> a0*u==s and b0*u==t
    True
    '''
    u = None
    while True:
        u = create_random_vector()
        if a0 * u == s and b0 * u == t:
            return u


def create_random_vector():
    return list2vec([randGF2() for l in a0.D])

## 2: (Task 7.7.2) Finding Secret Sharing Vectors
# Give each vector as a Vec instance

def find_vector_pairs():
    '''
    a0 and b0 are given. Find 4 other pairs, 8 other vectors, over GF2 where any 3 pairs are linearly independent
    :return: list of 5 vector tuple pairs (a0, b0) first
    >>> pairs = find_vector_pairs()
    >>> len(pairs) == 5
    True
    >>> pairs[0] == (a0, b0)
    True
    '''
    candidates = None
    while True:
        candidates = [(a0, b0)]
        for n in range(4):
            candidates.append((create_random_vector(), create_random_vector()))
        # pprint([combo for combo in combinations(candidates, 3)])
        if all(is_independent(list(chain.from_iterable(pair for pair in combo))) for combo in combinations(candidates, 3)):
            return candidates

pairs = find_vector_pairs()

secret_a0 = pairs[0][0]
secret_b0 = pairs[0][1]
secret_a1 = pairs[1][0]
secret_b1 = pairs[1][1]
secret_a2 = pairs[2][0]
secret_b2 = pairs[2][1]
secret_a3 = pairs[3][0]
secret_b3 = pairs[3][1]
secret_a4 = pairs[4][0]
secret_b4 = pairs[4][1]

