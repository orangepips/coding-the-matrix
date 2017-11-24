from itertools import permutations, combinations
import pprint
from vecutil import list2vec
from matutil import listlist2mat


def hamming_code_two_bit_error_collisions():
    """
    Demonstrate Hamming code doesn't allow recipient to correct two-bit errors
    by returning a set of two-tuples of different error vectors that solve H * e1 = H * e2
    :return: {(e1, e2), ...}

    >>> e1 = list2vec([1, 1, 0, 0, 0, 0, 0])
    >>> e2 = list2vec([0, 0, 1, 0, 0, 0, 0])
    >>> collisions = hamming_code_two_bit_error_collisions()
    >>> (e1, e2) in collisions or (e2, e1) in collisions
    True
    >>> e1 = list2vec([0, 0, 1, 0, 0, 1, 0])
    >>> e2 = list2vec([0, 1, 0, 0, 0, 0, 1])
    >>> (e1, e2) in collisions or (e2, e1) in collisions
    True
    """
    collisions = set()

    H = listlist2mat([
        [0, 0, 0, 1, 1, 1, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1]
    ])
    # TODO: make more efficient by only looking at 2x 2 bit error code and 1/2 bit error code combos
    error_codes = list({list2vec(e2) for e2 in set(permutations([0, 0, 0, 0, 0, 1, 1]))} | \
                  {list2vec(e1) for e1 in set(permutations([0, 0, 0, 0, 0, 0, 1]))})

    for e1_ix, e1 in enumerate(error_codes):
        for e2 in error_codes[e1_ix+1:]:
            if H * e1 == H * e2: collisions.add((e1, e2))

    return collisions