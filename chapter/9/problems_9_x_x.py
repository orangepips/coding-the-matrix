from resources.orthogonalization import *
from resources.vecutil import *

"""
Problem 9.2.2

b = [1, 1, 1]
vlist = [ [0, 2, 2], [0, 1, -1] ]

w = [0, 0, 0]

vlist[0] -> [0, 2, 2]
sigma0  = ([1, 1, 1] * [0, 2, 2]) / ([0, 2, 2] * [0, 2, 2])
        = 4 / 8
        = 1 / 2

sigma0 ->
w0      = sigma0 * vlist[0]
        = (1/2) * [0, 2, 2]
        = [0, 1, 1]

b0      = b - w0
        = [1, 1, 1] - [0, 1, 1]
        = [1, 0, 0]

vlist[1] -> [0, 1, -1]
sigma1  = ([1, 0, 0] * [0, 1, -1]) / ([0, 1, -1] * [0, 1, -1])
        = (1*0 + 0*1 + 0*-1) / (0*0, 1*1, -1*-1)
        = (0 + 0 + 0) / (0 + 1 + 1)
        = 0 / 2
        = 0

sigma1 ->
w1      = sigma1 * vlist[1]
        = 0 * [0, 1, -1]
        = [0, 0, 0]
        
b2      = b1 - w1
        = [1, 0, 0] - [0, 0, 0]
        = [1, 0, 0]
"""

def test_9_2_2(b, vlist):
    """
    Validate project_orthogonal
    :param b: n vector
    :param vlist: list of n vectors mutually orthogonal
    :return: projection of b orthgonal to vlist Vecs
    >>> b = list2vec([1, 1, 1])
    >>> vlist = [list2vec(l) for l in [[0, 2, 2], [0, 1, -1]]]
    >>> test_9_2_2(b, vlist) == list2vec([1, 0, 0])
    True
    """
    return project_orthogonal(b, vlist)

"""
Problem 9.3.4
v1 = [1, 0, 2]
v2 = [1, 0, 2]
v3 = [2, 0, 0]

v1, []
v*1     = v1
        = [1, 0, 2]

v2, [v*1]
v*2     = v2 - project_along(v2, v1*)
        = v2 - (<v2, v1*> / <v1*, v1*>) * v1*
        = [1, 0, 2] - ( ([1, 0, 2] * [1, 0, 2]) / ([1, 0, 2] * [1, 0, 2]) ) * [1, 0, 2]
        = [1, 0, 2] - ( ( 1*1 + 0*0 + 2*2 ) / ( 1*1 + 0*0 + 2*2 ) ) * [1, 0, 2]
        = [1, 0, 2] - ( 5 / 5 ) * [1, 0, 2]
        = [0, 0, 0] 

v3, [v*1, v*2]        
v*3_1   = v3 - project_along(v3, v*1)
        = [2, 0, 0] - ( ([2, 0, 0] * [1, 0, 2]) / ([1, 0, 2] * [1, 0, 2]) ) * [1, 0, 2]
        = [2, 0, 0] - ( (2*1 + 0*0 + 0*1) / (1*1 + 0*0 + 2*2) ) * [1, 0, 2]
        = [2, 0, 0] - ( 2 / 5 ) * [1, 0, 2]
        = [2, 0, 0] - [2/5, 0, 4/5]
        = [8/5, 0, -4/5]
v*3     = v*3_1 - project_along(v*3_1, v*2)
        = [8/5, 0, -4/5] - ( ([8/5, 0, -4/5] * [0, 0, 0] ) / ([0, 0, 0]  * [0, 0, 0] ) ) * [0, 0, 0] 
        = [8/5, 0, -4/5]
        
v*      = [ [1, 0, 2], [0, 0, 0], [8/5, 0, -4/5] ]
"""
def test_9_3_4(vlist):
    """
    :param vlist: m list of n vectors
    :return: m list of n vectors that are mutually orthogonal
    >>> vlist = [list2vec(l) for l in [[1, 0, 2], [1, 0, 2], [2, 0, 0]]]
    >>> vstarlist = [list2vec(l) for l in [[1, 0, 2], [0, 0, 0], [8/5, 0, -4/5]]]
    >>> test_9_3_4(vlist) == vstarlist
    True
    """
    return orthogonalize(vlist)