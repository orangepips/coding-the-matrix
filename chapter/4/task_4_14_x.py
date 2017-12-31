from resources.GF2 import one
from resources.matutil import listlist2mat, mat2coldict
from resources.vecutil import list2vec
from itertools import product
from resources.mat import Mat
from resources.vec import Vec

# Task 4.14.1
# 7 x 4
G = listlist2mat([
        [one, 0, one, one],
        [one, one, 0, one],
        [0, 0, 0, one],     #2: e3
        [one, one, one, 0],
        [0, 0, one, 0],     #4: e2
        [0, one, 0, 0],     #5: e1
        [one, 0, 0, 0]      #6: e0
    ])

# Task 4.14.1 & 2
def encode(p):
    """
    Encode p
    :param p: 4 vector message
    :return: 7 vector
    >>> p = list2vec([one, 0, 0, one])
    >>> encoding = encode(p)
    >>> encoding == list2vec([0, 0, one, one, 0, 0, one])
    True
    """
    return G * p

"""
Section 4.14.4
Note that four of the rows of G are the standard basis vectors e1, e2, e3, e4 of GF(2)4. What does that imply about
the relation between words and codewords? Can you easily decode the codeword [0, 1, 1, 1, 1, 0, 0] without using a
computer?

codeword: [0, 1, 1, 1, 1, 0, 0]
0:
1:
2: [x, x, x, 1]
3:
4: [x, x, 1, x]
5: [x, 0, x, x]
6: [0, x, x, x]
prediction [0, 0, 1, 1]
"""

"""
Example 4.6.2
M = [ 
    [1, 2], 
    [3, 4], 
    [10, 0]
]
v = [3, -1]

M * v   = [[1, 2] · [3, −1], [3, 4] · [3, −1], [10, 0] · [3, −1]]
        = [1 · 3 + 2 · -1, 3 · 3 + 4 · -1, 10 · 3 + 0 · -1]
        = [3 - 2, 9 - 4, 30 + 0]
        = [1, 5, 30]
"""

def compute_R():
    """
    Note that R can be one of several different combinations of rows.
    :return: a matrix that can decode 7-vector G encoded 4-vector messages
    """
    message_and_codeword = {message: encode(list2vec(message)) for message in product([0, one], repeat=4)}
    decoding_candidates = {list2vec(prdct) for prdct in product([0, one], repeat=7)}

    R_row_candidates = {
        0: decoding_candidates.copy(),
        1: decoding_candidates.copy(),
        2: decoding_candidates.copy(),
        3: decoding_candidates.copy()
    }

    for row in R_row_candidates:
        for message, codeword in message_and_codeword.items():
            message_bit = message[row]
            for decoding_candidate in decoding_candidates:
                if decoding_candidate not in R_row_candidates[row]: continue
                # print(row, message_bit, repr(decoding_candidate.f), repr(encoding.f), decoding_candidate * encoding)
                if not decoding_candidate * codeword == message_bit:
                    R_row_candidates[row].remove(decoding_candidate)

    result = Mat(
        (G.D[1], set(range(7))),
        {(row, col): list(R_row_candidates[row])[0][col] for row in R_row_candidates for col in
         list(R_row_candidates[row])[0].D}
    )

    for message, codeword in message_and_codeword.items():
        if not result * codeword == list2vec(message):
            raise Exception("{0} != {1}\nfor R {2}".format(result * codeword, list2vec(message), result))

    return result

# print(repr(compute_R()))
# print(R * G == identity(set(range(4)), one))

# Task 4.14.3
def decode(c, R = compute_R()):
    """
    Decode c
    :param c: 7 vector codeword
    :return: 4 vector

    >>> decode(list2vec([0, one, one, one, one, 0, 0])) == list2vec([0, 0, one, one])
    True
    """
    return R * c


H = listlist2mat([
    [0,     0,      0,      one,    one,    one,    one],
    [0,     one,    one,    0,      0,      one,    one],
    [one,   0,      one,    0,      one,    0,      one]
])

# print(repr(H*G))
# all zeros

# print(listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]]))
# print(Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 3): 0, (3, 0): 0, (2, 1): 0, (6, 2): 0, (5, 1): one, (0, 3): 0, (4, 0): 0, (1, 2): 0, (3, 3): 0, (6, 3): 0, (5, 0): 0, (2, 2): 0, (4, 1): 0, (1, 1): 0, (3, 2): one, (0, 0): 0, (6, 0): 0, (2, 3): 0, (4, 2): 0, (1, 0): 0, (5, 3): 0, (0, 1): 0, (6, 1): 0, (3, 1): 0, (2, 0): 0, (4, 3): one, (5, 2): 0, (0, 2): 0}))

def find_error(syndrome):
    """
    Input: an error syndrome as an instance of Vec
    Output: the corresponding error vector e
    Examples:
        >>> find_error(Vec({0,1,2}, {0:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{3: one})
        True
        >>> find_error(Vec({0,1,2}, {2:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{0: one})
        True
        >>> find_error(Vec({0,1,2}, {1:one, 2:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{2: one})
        True
        >>> find_error(Vec({0,1,2}, {})) == Vec({0,1,2,3,4,5,6}, {})
        True
    """
    result = Vec(H.D[1], {})
    cd = mat2coldict(H)
    for c, v in cd.items():
        if syndrome == v:
            result[c]=one
            break
    return result

S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])

print(
    Mat((H.D[1], S.D[1]), {(coords[0],coords[1]):one for coords in
        [t for t in
        [
            (next(iter(find_error(S_v).f.keys() or []), None), S_c)
                for S_c, S_v in mat2coldict(S).items()
        ] if not t[1] == None]}
    )
)

# print(Mat((H.D[1], S.D[1]),
#         {([k for k, v in S_v.f.items() if v == 0][0], S_c):one for S_c, S_v in mat2coldict(S).items()}))

print(Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}),
     {(1, 3): 0, (3, 0): 0, (2, 1): 0, (6, 2): 0, (5, 1): one, (0, 3): 0, (4, 0): 0,
      (1, 2): 0, (3, 3): 0, (6, 3): 0, (5, 0): 0, (2, 2): 0, (4, 1): 0, (1, 1): 0,
      (3, 2): one, (0, 0): 0, (6, 0): 0, (2, 3): 0, (4, 2): 0, (1, 0): 0, (5, 3): 0,
      (0, 1): 0, (6, 1): 0, (3, 1): 0, (2, 0): 0, (4, 3): one, (5, 2): 0, (0, 2): 0})
      )
