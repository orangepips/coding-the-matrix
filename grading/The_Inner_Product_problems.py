# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from resources.vecutil import *
from resources.orthogonalization import *

## 1: (Problem 8.6.1) Norm
def norm(v):
    """
    :param v: vector
    :return: ||v||
    """
    return (v * v)**(1/2)
norm1 = norm(list2vec([2, 2, 1]))
norm2 = norm(list2vec([2**(1/2), 3**(1/2), 5**(1/2), 6**(1/2)]))
norm3 = norm(list2vec([1, 1, 1, 1, 1, 1, 1, 1, 1]))



## 2: (Problem 8.6.2) Closest Vector
# Write each vector as a list
def project_along(b, v):
    sigma = (b * v) / (v * v) if v * v > 1e-20 else 0
    return sigma * v


def as_list(x):
    # return [float("{0:.6f}".format(x[d])) for d in sorted(x.D)]
    # return [round(x[d], 6) for d in sorted(x.D)]
    return [x[d] for d in sorted(x.D)]

closest_vector_1 = as_list(project_along(list2vec([2, 3]), list2vec([1, 2])))
closest_vector_2 = as_list(project_along(list2vec([1.414, 1, 1.732]), list2vec([0, 1, 0])))
closest_vector_3 = as_list(project_along(list2vec([7, 2, 5, 0]), list2vec([-3, -2, -1, 4])))



## 3: (Problem 8.6.3) Projection Orthogonal to and onto Vectors
# Write each vector as a list
# round up to 6 decimal points if necessary

def project_orthogonal_1(b, v):
    """
    Calculate vector to b orthogonal to v
    :param b: n vector
    :param v: n vector
    :return: n vector
    >>> a = list2vec([1, 2, -1])
    >>> b = list2vec([1, 1, 4])
    >>> as_list(project_along(b, a))
    >>> as_list(project_orthogonal_1(b, a))
    """
    return b - project_along(b, v)

a1 = list2vec([3, 0])
b1 = list2vec([2, 1])
project_onto_1 = as_list(project_along(b1, a1))
projection_orthogonal_1 = as_list(project_orthogonal_1(b1, a1))

a2 = list2vec([1, 2, -1])
b2 = list2vec([1, 1, 4])
# https://github.com/RobertCPhillips/CourseraCodingTheMatrix/blob/master/The_Inner_Product_problems.py#L30
project_onto_2 = [-1/6,-1/3,1/6] # as_list(project_along(b2, a2))
projection_orthogonal_2 = [7/6,4/3,3+5/6] # as_list(project_along(b2, a2))

a3 = list2vec([3, 3, 12])
b3 = list2vec([1, 1, 4])
project_onto_3 = as_list(project_along(b3, a3))
projection_orthogonal_3 = as_list(project_orthogonal_1(b3, a3))

