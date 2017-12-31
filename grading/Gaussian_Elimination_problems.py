# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

from resources.matutil import *
from resources.GF2 import one
from resources.vecutil import zero_vec
from resources.echelon import transformation


## 1: (Problem 7.9.2) Recognizing Echelon Form
# Write each matrix as a list of row lists

# Definition 7.1.1: An m × n matrix A is in echelon form if it satisfies the following condition: for any row, if that
# row’s first nonzero entry is in position k then every previous row’s first nonzero entry is in some position less
# than k.

# If a row of a matrix in echelon form is all zero then every subsequent row must also be all zero...

echelon_form_1 = [[1, 2, 0, 2, 0],
                  [0, 1, 0, 3, 4],
                  [0, 0, 2, 3, 4],
                  [0, 0, 0, 2, 0],
                  [0, 0, 0, 0, 4]]

echelon_form_2 = [[0, 4, 3, 4, 4],
                  [0, 0, 4, 2, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0]]

echelon_form_3 = [[1, 0, 0, 1],
                  [0, 0, 0, 1],
                  [0, 0, 0, 0]]

echelon_form_4 = [[1, 0 ,0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]



## 2: (Problem 7.9.3) Is it echelon?
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
        >>> is_echelon([[1,1]])
        True
        >>> is_echelon([[1]])
        True
        >>> is_echelon([[1],[1]])
        False
        >>> is_echelon([[0]])
        True
        >>> is_echelon([[0],[1]])
        False
        >>> is_echelon([[0, 0], [1, 0], [0, 1]])
        False
    '''
    first_non_zero_idx_per_row = []
    cols = len(A[0])
    rows = len(A)

    for irow in range(rows):
        row_non_zero_entry_idx = None
        for icol in range(cols):
            v = A[irow][icol]
            if v != 0:
                row_non_zero_entry_idx = icol
                break
        first_non_zero_idx_per_row.append(row_non_zero_entry_idx)
        if irow > 0:
            prior_row_non_zero_entry_idx = first_non_zero_idx_per_row[irow - 1]
            if row_non_zero_entry_idx != None and (prior_row_non_zero_entry_idx == None or \
                row_non_zero_entry_idx <= prior_row_non_zero_entry_idx):
                    return False

    return True


# NOTE: for 7.9.4 and 7.9.5 I used solver.solve. Remember to take the result and multiply the matrix to check
# e.g. M = listlist2mat(...), V = list2vec([...]), b = solve(M, V), M * b - V (is almost zero)

## 3: (Problem 7.9.4) Solving with Echelon Form: No Zero Rows
# Give each answer as a list

echelon_form_vec_a = [1, 0, 3, 0]
echelon_form_vec_b = [-3, 0, -2, 3]
echelon_form_vec_c = [-5, 0, 2, 0, 2]


## 4: (Problem 7.9.5) Solving with Echelon Form
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None" (without the quotes).

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21, 0, 2, 0, 0]


## 5: (Problem 7.9.6) Echelon Solver
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    True
    >>> U_rows = [ \
        Vec(D, {'A': one, 'C': one, 'D': one}), \
        Vec(D, {'B': one, 'E': one}), \
        Vec(D, {'C': one, 'E': one}), \
        Vec(D, {'E': one}) \
    ]
    >>> b_list = [one, 0, one, one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) == Vec(D,{'A': one, 'B': one, 'E': one})
    True
    >>> U_rows = [ \
        Vec(D, {'A': one, 'B': one, 'D': one}), \
        Vec(D, {'B': one, 'D': one, 'E': one}), \
        Vec(D, {'C': one, 'E': one}), \
        Vec(D, {}) \
    ]
    >>> b_list = [one, 0, one, 0]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) == Vec(D,{'A': one, 'C': one})
    True
    '''
    x = zero_vec(rowlist[0].D)
    b_rev = list(reversed(b))
    for ixrow, row in enumerate(reversed(rowlist)):
        non_zero_labels = [label for label in label_list if row[label] != 0]
        if not len(non_zero_labels): continue
        x[non_zero_labels[0]] = b_rev[ixrow] - sum([x[label] * row[label] for label in label_list])
        # print("ixrow: {0}\tnon_zero_labels: {1}\tb: {2}\tsum: {3}\trow: {4}\tx: {5}".format(ixrow, non_zero_labels, b[ixrow], sum([x[label] * one for label in non_zero_labels[1:]]), repr(row), repr(x)))
    return x


## 6: (Problem 7.9.7) Solving General Matrices via Echelon
def solve(A, b):
    """
    :param A: Matrix R x C
    :param b: Vector R
    :return: Vector C 'x' solving Ax=b
    >>> M = Mat(({'a', 'b', 'c', 'd'}, {'A', 'B', 'C', 'D'}), { \
        ('a', 'A'): one, ('a', 'B'): one, ('a', 'D'): one, \
        ('b', 'A'): one, ('b', 'D'): one, \
        ('c', 'A'): one, ('c', 'B'): one, ('c', 'C'): one, ('c', 'D'): one, \
        ('d', 'C'): one, ('d', 'D'): one \
    })
    >>> v = Vec(M.D[0], {'a': one, 'c': one})
    >>> solve(M, v)
    """
    M = transformation(A)
    U = M*A
    col_label_list = sorted(A.D[1])
    U_rows_dict = mat2rowdict(U)
    row_list = [U_rows_dict[i] for i in sorted(U_rows_dict)]
    # return echelon_solve(row_list,col_label_list, M*b)
    # print(row_list, col_label_list, repr(M * b))
    return row_list, col_label_list, M * b


M = Mat(({'a', 'b', 'c', 'd'}, {'A', 'B', 'C', 'D'}), {
    ('a', 'A'): one, ('a', 'B'): one, ('a', 'D'): one,
    ('b', 'A'): one, ('b', 'D'): one,
    ('c', 'A'): one, ('c', 'B'): one, ('c', 'C'): one, ('c', 'D'): one,
    ('d', 'C'): one, ('d', 'D'): one
})
v = Vec(M.D[0], {'a': one, 'c': one})
echelon_solve_args = solve(M, v)

row_list = echelon_solve_args[0]    # Provide as a list of Vec instances
label_list = echelon_solve_args[1] # Provide as a list
b = [echelon_solve_args[2][label] for label in sorted(echelon_solve_args[2].D)]        # Provide as a list of GF(2) values


A7 =  Mat(({'a', 'b', 'c', 'd', 'e'}, {'A', 'B', 'C', 'D', 'E'}), {
    ('a', 'D'): one,
    ('b', 'D'): one, ('b', 'E'): one,
    ('c', 'A'): one, ('c', 'D'): one,
    ('d', 'A'): one, ('d', 'E'): one,
    ('e', 'A'): one
})
M7 = Mat(({0, 1, 2, 3, 4}, A7.D[0]), {
    (0, 'c'): one,
    (1, 'a'): one,
    (2, 'a'): one, (2, 'b'): one,
    (3, 'b'): one, (3, 'c'): one, (3, 'd'): one,
    (4, 'a'): one, (4, 'c'): one, (4, 'e'): one
})
MA7 = Mat((M7.D[0], A7.D[1]), {
    (0, 'A'): one, (0, 'D'): one,
    (1, 'D'): one,
    (2, 'E'): one
})
def rows_of_M_times_A_equaling_zero_vec(M, A):
    """
    Determine rows u of M such that u * A = 0 (Note that these are vectors in the null space of the transpose A^T)
    :param M: P (rows) x Q (cols) matrix
    :param A: R x P matrix
    :return: set row numbers of M
    >>> rows_of_M_times_A_equaling_zero_vec(M7, A7)
    {3, 4}
    >>> rows_of_M_times_A_equaling_zero_vec(M8, A8)
    {4}
    """
    zv = zero_vec(A.D[1])
    return {k for k, v in mat2rowdict(M).items() if v * A == zv}


## 7: (Problem 7.9.8) Nullspace A
null_space_rows_a = rows_of_M_times_A_equaling_zero_vec(M7, A7) # Put the row numbers of M from the PDF


A8 =  Mat(({'a', 'b', 'c', 'd', 'e'}, {'A', 'B', 'C', 'D', 'E'}), {
    ('a', 'D'): one,
    ('b', 'D'): one, ('b', 'E'): one,
    ('c', 'A'): one, ('c', 'D'): one,
    ('d', 'A'): one, ('d', 'B'): one, ('d', 'C'): one, ('d', 'E'): one,
    ('e', 'A'): one, ('e', 'D'): one
})
M8 = Mat(({0, 1, 2, 3, 4}, A7.D[0]), {
    (0, 'c'): one,
    (1, 'c'): one, (1, 'd'): one,
    (2, 'a'): one,
    (3, 'a'): one, (3, 'b'): one,
    (4, 'c'): one, (4, 'e'): one
})
## 8: (Problem 7.9.9) Nullspace B
null_space_rows_b = rows_of_M_times_A_equaling_zero_vec(M8, A8) # Put the row numbers of M from the PDF

