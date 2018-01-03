# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from resources.mat import *
from resources.matutil import *
from resources.vec import *
from resources.vecutil import *
from resources.cancer_data import *

file_path = "../resources/data/"
training_file = file_path + "train.data"
validate_file = file_path + "validate.data"

# 8.4.1
def read_data_into_A_b(fname=training_file):
    """
    Read training data and produce:
    A: Matrix whose row labels are patient identification numbers and whose column
    labeled set is D
    b: a vector whose domain is the set of patient identification numbers, and b[r] is 1 if the
    specimen of patient r is malignant and -1 if the specim is benign
    :param fname: path and filename of breast cancer training data
    :return: A, b
    >>> A, b = read_data_into_A_b()
    >>> A.D[0] == b.D
    True
    """
    return read_training_data(fname)


## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    return Vec(u.D, {d: (1 if u[d] >= 0 else -1) for d in u.D})

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> fraction_wrong(A, b, w)
        0.3333333333333333
        >>> A = Mat(({'a','b','c', 'd', 'e'},{'A','B'}), {\
            ('a','A'):-4, ('a','B'):3, \
            ('b','A'):1, ('b','B'):8, \
            ('c','A'):5, ('c','B'):2, \
            ('d','A'):2, ('d','B'):-3, \
            ('e','A'):2, ('d','B'):-3 \
        })
        >>> b = Vec({'a','b','c', 'd', 'e'}, {'a':1, 'b':-1,'c':1, 'd': -1, 'e': -1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> fraction_wrong(A, b, w)

    '''
    # (a1) dot_product = positive_count - negative_count
    # (a2) positive_count = dot_product + negative_count

    # (b1) total = positive_count + negative_count
    # (b2) negative_count = total - positive_count

    # (a3) positive_count = dot_product + (total - positive_count) <- (b2)
    # (a4) 2 * positive_count = dot_product + total
    # (a5) positive_count = (dot_product + total) / 2

    # (b) negative_count = total - ((dot_product + total) / 2) <- (a5)

    total = len(b.D)
    dot_product = signum(A * w) * b
    positive_count = (dot_product + total) / 2
    negative_count = total - positive_count
    return  negative_count / total

## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> loss(A, b, w)
        317
    '''
    return (A * w - b) * (A * w - b)

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> find_grad(A, b, w) == Vec({'B', 'A'},{'B': -290, 'A': 60})
        True
    '''
    return 2 * ((A * w - b) * A)

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> sigma = .1
        >>> gradient_descent_step(A, b, w, sigma) == Vec({'B', 'A'},{'B': 27.0, 'A': -5.0})
        True
    '''
    return w - sigma * find_grad(A, b, w)

## Ungraded task ##
def gradient_descent(A, b, w, sigma, T):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
        - T: number of iterations to run
    Output: hypothesis vector obtained after T iterations of gradient descent.
    >>> sigma = 10**-9
    >>> T = 300
    >>> A, b = read_data_into_A_b()
    >>> w_zero = zero_vec(A.D[1])
    >>> hypothesis_vector = gradient_descent(A, b, w_zero, sigma, T)
    >>> A_val, b_val = read_data_into_A_b(validate_file)
    >>> fraction_wrong(A_val, b_val, hypothesis_vector) <= fraction_wrong(A, b, hypothesis_vector) * 1.25 # 25% increase
    True

    # >>> w_ones = Vec(A.D[1], {d:1 for d in A.D[1]})
    # >>> print(gradient_descent(A, b, w_ones, sigma, T))
    '''
    _STATUS_INCREMENT = 30
    _LOOP_COUNTER = 0
    while True:
        w = gradient_descent_step(A, b, w, sigma)
        _LOOP_COUNTER += 1
        if _LOOP_COUNTER % _STATUS_INCREMENT == 0 or _LOOP_COUNTER >= T:
            print("{0}: Loss: {1}\tFraction Wrong: {2}".format(_LOOP_COUNTER, loss(A, b, w), fraction_wrong(A, b, w)))
        if _LOOP_COUNTER >= T:
            break
    return w
