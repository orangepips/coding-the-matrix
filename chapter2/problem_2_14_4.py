import collections
from itertools import combinations

from vecutil import list2vec, zero_vec

from GF2 import one


def calc_combo_sums(codes, D):
    combo_sums = collections.defaultdict(set)
    keys = codes.keys()
    for i in range(2, len(keys) + 1):
        combos = combinations(keys, i)
        for combo in combos:
            combo_sum_vec = zero_vec(D)
            for key in combo:
                combo_sum_vec += codes[key]
            combo_sums[combo_sum_vec].add(tuple(combo))
    return combo_sums

def not_present_or_subset(vec, combo_sums):
    return repr(vec) + ":\t" + ("not present" if not vec in combo_sums else str(combo_sums[vec]))


def problem_2_14_4():
    codes = {
        'a': list2vec([one, one,    0,      0,      0,      0,      0]),
        'b': list2vec([0,   one,    one,    0,      0,      0,      0]),
        'c': list2vec([0,   0,      one,    one,    0,      0,      0]),
        'd': list2vec([0,   0,      0,      one,    one,    0,      0]),
        'e': list2vec([0,   0,      0,      0,      one,    one,    0]),
        'f': list2vec([0,   0,      0,      0,      0,      one,    one])
    }

    u = list2vec([0, 0, one, 0, 0, one, 0])
    v = list2vec([0, one, 0, 0, 0, one, 0])

    combo_sums = calc_combo_sums(codes, u.D)

    print(not_present_or_subset(u, combo_sums))
    print(not_present_or_subset(v, combo_sums))

def problem_2_14_5():
    codes = {
        'a': list2vec([one, one,    one,    0,      0,      0,      0]),
        'b': list2vec([0,   one,    one,    one,    0,      0,      0]),
        'c': list2vec([0,   0,      one,    one,    one,    0,      0]),
        'd': list2vec([0,   0,      0,      one,    one,    one,    0]),
        'e': list2vec([0,   0,      0,      0,      one,    one,    one]),
        'f': list2vec([0,   0,      0,      0,      0,      one,    one])
    }

    u = list2vec([0, 0, one, 0, 0, one, 0])
    v = list2vec([0, one, 0, 0, 0, one, 0])

    combo_sums = calc_combo_sums(codes, u.D)

    print(not_present_or_subset(u, combo_sums))
    print(not_present_or_subset(v, combo_sums))

if __name__ == "__main__":
    problem_2_14_4()
    problem_2_14_5()






