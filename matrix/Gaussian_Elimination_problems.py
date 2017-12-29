# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one



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
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    pass



## 6: (Problem 7.9.7) Solving General Matrices via Echelon
rowlist = [ ... ]    # Provide as a list of Vec instances
label_list = [ ... ] # Provide as a list
b = [ ... ]          # Provide as a list of GF(2) values



## 7: (Problem 7.9.8) Nullspace A
null_space_rows_a = {...} # Put the row numbers of M from the PDF



## 8: (Problem 7.9.9) Nullspace B
null_space_rows_b = {...} # Put the row numbers of M from the PDF

