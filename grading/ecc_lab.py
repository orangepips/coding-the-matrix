# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

# 4.14.x from the book

from resources.vec import Vec
from resources.mat import Mat
from resources.bitutil import bits2mat, str2bits, noise, mat2bits
from resources.GF2 import one
from resources.matutil import listlist2mat, mat2coldict

## Task 1
""" Create an instance of Mat representing the generator matrix G. You can use
the procedure listlist2mat in the matutil module (be sure to import first).
Since we are working over GF (2), you should use the value one from the
GF2 module to represent 1"""
G = listlist2mat([
        [one, 0, one, one],
        [one, one, 0, one],
        [0, 0, 0, one],     #2: e3
        [one, one, one, 0],
        [0, 0, one, 0],     #4: e2
        [0, one, 0, 0],     #5: e1
        [one, 0, 0, 0]      #6: e0
    ])


## Task 2
# Please write your answer as a list. Use one from GF2 and 0 as the elements.
encoding_1001 = [0, 0, one, one, 0, 0, one]


## Task 3
# Express your answer as an instance of the Mat class.
R = Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}), {(1, 2): one, (3, 2): 0, (0, 0): one, (3, 0): one, (0, 4): one, (1, 4): 0, (2, 6): 0, (0, 5): 0, (2, 1): one, (2, 5): 0, (2, 0): 0, (1, 0): 0, (3, 5): 0, (0, 1): 0, (0, 2): one, (3, 3): 0, (0, 6): 0, (3, 4): one, (3, 1): 0, (1, 6): one, (1, 1): one, (1, 5): 0, (3, 6): one, (2, 2): one, (1, 3): 0, (2, 3): one, (0, 3): 0, (2, 4): 0})

## Task 4
# Create an instance of Mat representing the check matrix H.
H = listlist2mat([
    [0,     0,      0,      one,    one,    one,    one],
    [0,     one,    one,    0,      0,      one,    one],
    [one,   0,      one,    0,      one,    0,      one]
])

## Task 5
# 4.14.5
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

## Task 6
# Use the Vec class for your answers.
non_codeword = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one, 6:one})
error_vector = find_error(H * non_codeword)
code_word = non_codeword + error_vector
original = R * code_word


## Task 7
def find_error_matrix(S):
    """
    Input: a matrix S whose columns are error syndromes
    Output: a matrix whose cth column is the error corresponding to the cth column of S.
    Example:
        >>> S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
        >>> find_error_matrix(S) == Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 3): 0, (3, 0): 0, (2, 1): 0, (6, 2): 0, (5, 1): one, (0, 3): 0, (4, 0): 0, (1, 2): 0, (3, 3): 0, (6, 3): 0, (5, 0): 0, (2, 2): 0, (4, 1): 0, (1, 1): 0, (3, 2): one, (0, 0): 0, (6, 0): 0, (2, 3): 0, (4, 2): 0, (1, 0): 0, (5, 3): 0, (0, 1): 0, (6, 1): 0, (3, 1): 0, (2, 0): 0, (4, 3): one, (5, 2): 0, (0, 2): 0})
        True
    """
    return Mat((H.D[1], S.D[1]), {(coords[0],coords[1]):one for coords in
        [t for t in
        [
            (next(iter(find_error(S_v).f.keys() or []), None), S_c)
                for S_c, S_v in mat2coldict(S).items()
        ] if not t[1] == None]}
    )



## Task 8
s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it."
P = bits2mat(str2bits(s))

## Task 9
C = G*P
bits_before = len(mat2bits(P))
bits_after = len(mat2bits(G*P))


## Ungraded Task
CTILDE = C + noise(C, .02)

## Task 10
# TODO: determine why this fails when sent via submit.py
def correct(A):
    """
    Input: a matrix A each column of which differs from a codeword in at most one bit
    Output: a matrix whose columns are the corresponding valid codewords.
    Example:
        >>> A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
        >>> correct(A) == Mat(({0, 1, 2, 3, 4, 5, 6}, {1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (1, 3): 0, (3, 3): 0, (5, 2): one, (6, 1): 0, (3, 1): 0, (2, 1): 0, (0, 2): one, (6, 3): one, (4, 2): 0, (6, 2): one, (2, 3): 0, (4, 3): 0, (2, 2): 0, (5, 1): 0, (0, 3): one, (4, 1): 0, (1, 1): 0, (5, 3): one})
        True
    """
    return find_error_matrix(H * A) + A

