# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from resources.mat import Mat
from resources.vec import Vec
from resources.vecutil import *
from resources.matutil import *
from resources.orthogonalization import *
from resources.solver import solve
from resources.independence import rank
from grading.The_Inner_Product_problems import norm


## 1: (Problem 9.11.1) Generators for orthogonal complement
# https://github.com/jimcarson/Coursera/blob/master/CodingTheMatrix/hw21_orthogalization_problems/Orthogonalization_problems.py#L21
def find_orthogonal_complement(U_basis, W_basis):
    """
    Find the list of vectors that form the orthogonal complement of U with respect to W
    Vectors u*1..k have same span and are nonzero
    as u1..k is linearly independent.  n-k of the remaining vectors of
    w*1..n are nonzero and every one is orthogonal to u1..n, so they
    are orthogonal to every vector in U.
    :param U_basis: list of n vectors
    :param W_basis: list of n vectors
    :return: list of n vectors
    >>> L = [list2vec(v) for v in [[8, -2, 2], [0, 3, 3], [1, 0, 0], [0, 1, 1], [0, 0, 1]]]
    >>> all([(x-y).is_almost_zero() for x, y in zip(find_orthogonal_complement(L[:2], L[2:]), [list2vec([1/9, 2/9, -2/9])])])
    True
    >>> U_9_11_2_1 = [list2vec(v) for v in [[0, 0, 1], [1, 2, 0]]]
    >>> W_9_11_2_1 = [list2vec(v) for v in [[1, 0, 0], [1, 0, 1]]]
    >>> result = find_orthogonal_complement(U_9_11_2_1, W_9_11_2_1)

    """
    return [v for v in orthogonalize(U_basis + W_basis)[len(U_basis):] if not v.is_almost_zero()]

U_vecs_1 = [list2vec([0,0,3,2])]
W_vecs_1 = [list2vec(v) for v in [[1,2,-3,-1],[1,2,0,1],[3,1,0,-1],[-1,-2,3,1]]]
# Give a list of Vecs

ortho_compl_generators_1 = find_orthogonal_complement(U_vecs_1, W_vecs_1)

U_vecs_2 = [list2vec([3,0,1])]
W_vecs_2 = [list2vec(v) for v in [[1,0,0],[1,0,1]]]

# Give a list of Vecs
ortho_compl_generators_2 = find_orthogonal_complement(U_vecs_2, W_vecs_2)

U_vecs_3 = [list2vec(v) for v in [[-4,3,1,-2],[-2,2,3,-1]]]
W_vecs_3 = [list2vec(v) for v in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]]

# Give a list of Vecs
ortho_compl_generators_3 = find_orthogonal_complement(U_vecs_3, W_vecs_3)

# TODO: explain 9.11.2



## 2: (Problem 9.11.3) Basis for null space
# Your solution should be a list of Vecs
A_9_11_3 = listlist2mat([[-4, -1, -3, -2], [0, 4, 0, -1]])
def find_null_space_basis(A):
    """
    Let A be a R × C matrix over R. Recall that the null space of A is the set of C-vectors u such that Au is a zero
    vector. By the dot-product definition of matrix-vector multiplication, this is the set of C-vectors u whose
    dot-product with each row of A is zero. Since our inner product for vectors over R is dot-product, this means that
    the orthogonal complement of Row A in RC is Null A.
    :param A: RxC matrix
    :return: list of C vectors u, such that for row A[i] and u[i] is the zero vector
    >>> complement = find_null_space_basis(A_9_11_3)
    >>> all([c*a < 1e-10 for c in complement for a in list(mat2rowdict(A_9_11_3).values())])
    True
    """
    A_rows = list(mat2rowdict(A).values())
    I_cols = list(mat2coldict(identity(A.D[1], 1)).values())
    return find_orthogonal_complement(A_rows, I_cols)

null_space_basis = find_null_space_basis(A_9_11_3)


def test_find_normal(U, eps=1e-10):
    return all([u * n < eps for u in U for n in find_normal(U)])


def affine_hull(U):
    """
    :param U: list of n vectors
    :return: list of vectors such that [U[1] - U[0], ... U[n-1] - U[0]]
    """
    return [u - U[0] for u in U[1:]]


def find_normal(U):
    """
    :param U: list of n vectors
    :return: list of n vectors orthogonal to U
    >>> eps = 1e-10
    >>> test_find_normal([list2vec([3, 2])]) # 9.11.4 > 1
    True
    >>> test_find_normal([list2vec([3, 5])]) # 9.11.4 > 2
    True
    >>> test_find_normal([list2vec(v) for v in [[0, 1, 0], [0, 0, 1]]]) # 9.11.5 > 1
    True
    >>> test_find_normal([list2vec(v) for v in [[2, 1, -3], [-2, 1, 1]]]) # 9.11.5 > 2
    True
    >>> test_find_normal(affine_hull([list2vec(v) for v in [[3, 1, 4], [5, 2, 6], [2, 3, 5]]])) # 9.11.5 > 3
    True
    """
    I_cols = list(mat2coldict(identity(U[0].D, 1)).values())
    return find_orthogonal_complement(U, I_cols)

# TODO: 9.11.6

def span_normal(span, n):
    """
    Validate a
    :param span: set of n vectors spanning a plane
    :param n: n vector that is the normal of span
    :return: boolean indicating if n is the normal of the span
    >>> span_1 = [list2vec(l) for l in [[1, 0, 0], [0, 1, -1], [0, -1, 1]]] # 9.11.7 > 1
    >>> n_1 = list2vec([0, 1, 1])
    >>> span_normal(span_1, n_1)
    True
    >>> span_2 = [list2vec(l) for l in [[1, 0, 1]]] # 9.11.7 > 2
    >>> n_2 = list2vec([0, 1, 0])
    >>> span_normal(span_2, n_2)
    True
    """
    return all([s*n == 0 for s in span])


def rank_theorem_alternate(A):
    """
    p 335
    Equivalently, the row rank of M is the dimension of Row M, and the column rank of M is the dimension of Col M.
    :param A: matrix
    :return: (count A rows, count a cols)
    >>> rank_theorem_alternate(identity(set(range(5)), 1))
    (5, 5)
    >>> rank_theorem_alternate(listlist2mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    (3, 3)
    """
    A_rows = list(mat2rowdict(A).values())
    A_cols = list(mat2coldict(A).values())

    null_space_basis_A = find_null_space_basis(A)
    null_space_basis_A = [zero_vec(A.D[1])] if len(null_space_basis_A) == 0 else null_space_basis_A

    Null_A = rowdict2mat(null_space_basis_A)
    Null_A_rows = list(mat2rowdict(Null_A).values())
    Null_A_cols = list(mat2coldict(Null_A).values())

    num_A_cols = rank(A_cols) + rank(Null_A_cols)

    num_A_rows = rank(A_rows) + rank(Null_A_rows)

    return num_A_rows, num_A_cols


## 3: (Problem 9.11.9) Orthonormalize(L)
def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list Lstar of len(L) orthonormal Vecs such that, for all i in range(len(L)),
            Span L[:i+1] == Span Lstar[:i+1]

    >>> from vec import Vec
    >>> D = {'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> for v in orthonormalize(L): print(v)
    ... 
    <BLANKLINE>
        a     b     c     d
    -----------------------
     0.73 0.548 0.183 0.365
    <BLANKLINE>
         a     b      c      d
    --------------------------
     0.187 0.403 -0.566 -0.695
    <BLANKLINE>
         a      b      c     d
    --------------------------
     0.528 -0.653 -0.512 0.181
    '''
    return [(1 / norm(v)) * v for v in orthogonalize(L)]




## 4: (Problem 9.11.10) aug_orthonormalize(L)
def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist of lists such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
            
    >>> from vec import Vec
    >>> D={'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> Qlist, Rlist = aug_orthonormalize(L)
    >>> from matutil import coldict2mat
    >>> print(coldict2mat(Qlist))
    <BLANKLINE>
               0      1      2
         ---------------------
     a  |   0.73  0.187  0.528
     b  |  0.548  0.403 -0.653
     c  |  0.183 -0.566 -0.512
     d  |  0.365 -0.695  0.181
    <BLANKLINE>
    >>> print(coldict2mat(Rlist))
    <BLANKLINE>
              0    1      2
         ------------------
     0  |  5.48 8.03   9.49
     1  |     0 11.4 -0.636
     2  |     0    0   6.04
    <BLANKLINE>
    >>> print(coldict2mat(Qlist)*coldict2mat(Rlist))
    <BLANKLINE>
           0  1  2
         ---------
     a  |  4  8 10
     b  |  3  9  1
     c  |  1 -5 -1
     d  |  2 -5  5
    <BLANKLINE>
    '''

    Qlist = orthonormalize(L)
    # Rlist = list(mat2coldict(coldict2mat(Qlist).transpose() * coldict2mat(L)).values())
    Rm = coldict2mat(Qlist).transpose() * coldict2mat(L)
    for x in Rm.D[0]:
        for y in Rm.D[1]:
            Rm[x, y] = 0 if abs(Rm[x, y]) < 1e-10 else Rm[x, y]
    Rlist = list(mat2coldict(Rm).values())
    return Qlist, Rlist

# TODO: determine why this is suggested for 9.11.10
def adjust(v, multipliers):
    """
    :param v: Vec with domain {0, 1, 2, ..., n - 1}
    :param multipliers: n element list of scalars
    :return: Vec w with same domain as v such that w[i] = multipliers[i] * v[i]
    >>> v = list2vec([1, 2, 3])
    >>> m = [3, 2, 1]
    >>> adjust(v, m) == list2vec([3*1, 2*2, 1*3])
    True
    >>> v == list2vec([1, 2, 3])
    True
    """
    w = v.copy()
    for i in range(len(multipliers)):
        w[i] *= multipliers[i]
    return w



## 5: (Problem 9.11.11) QR factorization of small matrices
#Compute the QR factorization

#Please represent your solution as a list of rows, such as [[1,0,0],[0,1,0],[0,0,1]]

def my_qr_factor(A):
    """
    A = QR
    Q orthonormalized matrix as row list
    R triangular matrix as row list
    :param A: m (rows) x n (cols) matrix where m >= n
    :return: Q, R
    >>> A = listlist2mat([[6, 6], [2, 0], [3, 3]])
    >>> Q, R = my_qr_factor(A)
    >>> Qm = listlist2mat(Q)
    >>> Rm = listlist2mat(R)
    >>> all([v.is_almost_zero() for v in list(mat2coldict(Qm * Rm - A).values())])
    True
    """
    Qlist, Rlist = aug_orthonormalize(list(mat2coldict(A).values()))
    Qm = coldict2mat(Qlist)
    Rm = coldict2mat(Rlist)
    return [vec2list(q) for q in list(mat2rowdict(Qm).values())], [vec2list(r) for r in list(mat2rowdict(Rm).values())]

M_9_11_11_1 = listlist2mat([[6, 6], [2, 0], [3, 3]])

# part_1_Q = ...
# part_1_R = ...

part_1_Q, part_1_R = my_qr_factor(M_9_11_11_1)

M_9_11_11_2 = listlist2mat([[2, 3], [2, 1], [1, 1]])

# part_2_Q = ...
# part_2_R = ...

part_2_Q, part_2_R = my_qr_factor(M_9_11_11_2)

## 6: (Problem 9.11.12) QR Solve
from resources.matutil import mat2coldict, coldict2mat
from resources.python_lab import dict2list, list2dict
from resources.triangular import *

def QR_factor(A):
    col_labels = sorted(A.D[1], key=repr)
    Acols = dict2list(mat2coldict(A),col_labels)
    Qlist, Rlist = aug_orthonormalize(Acols)
    #Now make Mats
    Q = coldict2mat(Qlist)
    R = coldict2mat(list2dict(Rlist, col_labels))
    return Q,R


def QR_solve(A, b):
    '''
    Input:
        - A: a Mat with linearly independent columns
        - b: a Vec whose domain equals the set of row-labels of A
    Output:
        - vector x that minimizes norm(b - A*x)
    Note: This procedure uses the procedure QR_factor, which in turn uses dict2list and list2dict.
           You wrote these procedures long back in python_lab.  Make sure the completed python_lab.py
           is in your matrix directory.

    Ax = b
    QRx = b
    Q^t * Q * R * x = Q^t * b
    Rx = Q^t * b

    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR_factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = QR_solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result.is_almost_zero()
        True
    '''

    Q, R = QR_factor(A)
    R_rowlist = list(mat2rowdict(R).values())
    R_label_list = sorted(A.D[1], key=repr)
    return triangular_solve(R_rowlist, R_label_list, Q.transpose() * b)


## 7: (Problem 9.11.13) Least Squares Problem
# Please give each solution as a Vec

least_squares_A1 = listlist2mat([[8, 1], [6, 2], [0, 6]])
least_squares_Q1 = listlist2mat([[.8,-0.099],[.6, 0.132],[0,0.986]])
least_squares_R1 = listlist2mat([[10,2],[0,6.08]])
least_squares_b1 = list2vec([10, 8, 6])

def least_squares(A, b):
    """

    :param A: R x C matrix
    :param b: C vector
    :return: R vector x minimizing ||Ax - b||^2
    >>> least_squares_x_hat_1 = least_squares(least_squares_A1, least_squares_b1)
    >>> lease_squares_result_1 = least_squares_A1.transpose() * (least_squares_b1 - least_squares_A1 * least_squares_x_hat_1)
    >>> lease_squares_result_1.is_almost_zero()
    True
    """
    return QR_solve(A, b)

x_hat_1 = least_squares(least_squares_A1, least_squares_b1)


least_squares_A2 = listlist2mat([[3, 1], [4, 1], [5, 1]])
least_squares_Q2 = listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
least_squares_R2 = listlist2mat([[7.07, 1.7],[0,.346]])
least_squares_b2 = list2vec([10,13,15])

x_hat_2 = least_squares(least_squares_A2, least_squares_b2)



## 8: (Problem 9.11.14) Small examples of least squares
#Find the vector minimizing (Ax-b)^2

#Please represent your solution as a list

your_answer_1 = vec2list(QR_solve(listlist2mat([[8, 1], [6, 2], [0, 6]]), list2vec([10, 8, 6])))
your_answer_2 = vec2list(QR_solve(listlist2mat([[3, 1], [4, 1]]), list2vec([10, 13])))



## 9: (Problem 9.11.15) Linear regression example
#Find a and b for the y=ax+b line of best fit

from resources.read_data import read_vectors


def linear_data_to_A_b(filename="../resources/data/age-height.txt", x_label="age", y_label="height"):
    rows = read_vectors(filename)
    D = set(range(len(rows)))
    # print(D)
    A = Mat((D, {'a', 'b'}), {})
    b = zero_vec(D)
    # print(A)
    for ix, row in enumerate(rows):
        # print(ix)
        A[ix, 'b'] = 1
        A[ix, 'a'] = row[x_label]
        b[ix] = row[y_label]
    return A, b

def linear_regression(filename="../resources/data/age-height.txt", x_label="age", y_label="height"):
    """

    :param filename: file to read
    :param x_label:
    :param y_label:
    :return: a, b minimizing y=ax+b
    >>> x = linear_regression()
    >>> A, b = linear_data_to_A_b()
    >>> result = A.transpose() * (b - A * x)
    >>> result.is_almost_zero()
    True
    """
    A, b = linear_data_to_A_b(filename, x_label, y_label)

    return QR_solve(A, b)

v = linear_regression()

a = v['a']
b = v['b']

