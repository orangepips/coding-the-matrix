from itertools import combinations
import collections
import pprint

# also see Example 2.9.17

# def calculate_possible_requests(challenge, response, requests = None):
#     challenge_len = len(challenge)
#
#     if requests is None:
#         requests = set()
#         for n in range(2 ** 6 - 1):
#             requests.add('{0:0{1}b}'.format(n, challenge_len))
#
#     int_challenge = int(challenge, 2)
#     candidate_requests = requests.copy()
#
#     for candidate_request in candidate_requests:
#         int_dot_product = int_challenge ^ int(candidate_request, 2)
#         dot_product = '{0:0{1}b}'.format(int_dot_product,challenge_len)
#         dot_product_response = dot_product.count("1") % 2
#         keep = True
#         if not dot_product_response == response:
#             requests.remove(candidate_request)
#             keep = False
#
#         print("{0}\t{1}\t{2}\t{3}".format(candidate_request, dot_product, dot_product_response, keep))
#
#     return requests


CHALLENGE_LENGTH = 6

"""
Convert a binary string to an int 
"""
def bin2int(binary_string):
    return int(binary_string, 2)


def int2bin(i):
    return '{0:0{1}b}'.format(i, CHALLENGE_LENGTH)

# http://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
def calculate_combo_sums(observations):
    combo_sums = collections.defaultdict(set)
    int_observations = [bin2int(key) for key in observations.keys()]
    len_observations = len(observations)
    for i in range(2, len_observations+1):
        combos = combinations(int_observations, i)
        for combo in combos:
            combo_sum = 0
            for v in combo:
                combo_sum ^= v
            combo_sums[combo_sum].add(tuple(combo))

    return combo_sums

"""
Problem 2.9.29: Eve knows the following challenges and responses: 
challenge response 
110011 0 
101010 0 
111011 1 
001100 1 
Show how she can derive the right responses to the challenges 011101 and 000100.
"""
if __name__ == "__main__":
    observations = {
        "110011": 0,
        "101010": 0,
        "111011": 1,
        "001100": 1
    }

    challenges = ['011101', '000100']

    combo_sums = calculate_combo_sums(observations)
    # pprint.PrettyPrinter().pprint(combo_sums)

    for challenge in challenges:
        int_challenge = bin2int(challenge)
        # print(int_challenge)
        if int_challenge in combo_sums:
            match_combos = combo_sums[int_challenge]
        # print(match_combos)
        response = 0
        for match_combo in match_combos:
            for e in match_combo:
                observation_response = observations[int2bin(e)]
                # print(int2bin(e), observation_response)
                response ^= observations[int2bin(e)]
        print("{0}\t{1}".format(challenge, response))

    pass