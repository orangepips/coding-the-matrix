# version code d7da415c4b69+
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec
from matutil import mat2rowdict, mat2coldict, rowdict2mat, coldict2mat
from vecutil import list2vec


## 1: (Problem 4.17.1) Computing matrix-vector products
# Please represent your solution vectors as lists.
vector_matrix_product_1 = [1, 0]
vector_matrix_product_2 = [0, 4.44]
vector_matrix_product_3 = [14, 20, 26]



## 2: (Problem 4.17.2) Matrix-vector multiplication to swap entries
# Represent your solution as a list of rowlists.
# For example, the 2x2 identity matrix would be [[1,0],[0,1]].

M_swap_two_vector = [[0,1], [1,0]]



## 3: (Problem 4.17.3) [z+x, y, x] Matrix-vector multiplication
three_by_three_matrix = [
    [1,0,1],
    [0,1,0],
    [1,0,0]
] # Represent with a list of row lists.



## 4: (Problem 4.17.4) [2x, 4y, 3z] matrix-vector multiplication
multiplied_matrix = [
    [2,0,0],
    [0,4,0],
    [0,0,3]
] # Represent with a list of row lists.



## 5: (Problem 4.17.5) Matrix multiplication: dimension of matrices
# Please enter a boolean representing if the multiplication is valid.
# If it is not valid, please enter None for the dimensions.
# Ca == Rb
# Result: Ra, Cb

part_1_valid = False # True or False
part_1_number_rows = None # Integer or None
part_1_number_cols = None # Integer or None

part_2_valid = False
part_2_number_rows = None
part_2_number_cols = None

part_3_valid = True
part_3_number_rows = 1
part_3_number_cols = 2

part_4_valid = True
part_4_number_rows = 2
part_4_number_cols = 1

part_5_valid = False
part_5_number_rows = None
part_5_number_cols = None

part_6_valid = True
part_6_number_rows = 1
part_6_number_cols = 1

part_7_valid = True
part_7_number_rows = 3
part_7_number_cols = 3



## 6: (Problem 4.17.6) Matrix-matrix multiplication practice with small matrices
# Please represent your answer as a list of row lists.
# Example: [[1,1],[2,2]]
# Result: Ra, Cb

small_mat_mult_1 = [
    [2*1+3*2, 2*2+3*3],
    [4*1+2*2, 4*2+2*3]
]
small_mat_mult_2 = [
    [2*1+4*5+1*2,  2*2+4*1+1*3,  2*0+4*1+1*0],
    [3*1+0*5+-1*2, 3*2+0*1+-1*3, 3*0+0*1+-1*0]
]
small_mat_mult_3 = [
    [2*3+2*-2+1*1, 2*1+2*6+1*-1]
]
small_mat_mult_4 = [
    [1*1+2*2+3*3]
]
small_mat_mult_5 = [
    [1*1, 1*2, 1*3],
    [2*1, 2*2, 2*3],
    [3*1, 3*2, 3*3]
]
small_mat_mult_6 = [
    [ 4*-1 +  2*1,   4*1 +  2*0],
    [ 1*-1 +  2*1,   1*1 +  2*0],
    [-3*-1 + -2*1,  -3*1 + -2*0]
]



## 7: (Problem 4.17.7) Matrix-matrix multiplication practice with a permutation matrix
# Please represent your solution as a list of row lists.

part_1_AB = [
    [5, 2, 0, 1],
    [2, 1, -4, 6],
    [2, 3, 0, -4],
    [-2, 3, 4, 0]
]
part_1_BA = [
    [1, -4, 6, 2],
    [3, 0, -4, 2],
    [3, 4, 0, -2],
    [2, 0, 1, 5]
]

part_2_AB = [
    [5, 1, 0, 2],
    [2, 6, -4, 1],
    [2, -4, 0, 3],
    [-2, 0, 4, 3]
]
part_2_BA = [
    [3, 4, 0, -2],
    [3, 0, -4, 2],
    [1, -4, 6, 2],
    [2, 0, 1, 5]
]

part_3_AB = [
    [1, 0, 5, 2],
    [6, -4, 2, 1],
    [-4, 0, 2, 3],
    [0, 4, -2, 3]
]
part_3_BA = [
    [3, 4, 0, -2],
    [1, -4, 6, 2],
    [2, 0, 1, 5],
    [3, 0, -4, 2]
]



## 8: (Problem 4.17.9) Matrix-matrix multiplication practice with very sparse matrices
# Please represent your answer as a list of row lists.

your_answer_a_AB = [
    [0, 0, 2, 0],
    [0, 0, 5, 0],
    [0, 0, 4, 0],
    [0, 0, 6, 0]
]
your_answer_a_BA = [
    [0, 0, 0, 0],
    [4, 4, 4, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

your_answer_b_AB = [
    [0, 2, -1, 0],
    [0, 5, 3, 0],
    [0, 4, 0, 0],
    [0, 6, -5, 0]
]
your_answer_b_BA = [
    [0, 0, 0, 0],
    [1, 5, -2, 3],
    [0, 0, 0, 0],
    [4, 4, 4, 0]
]

your_answer_c_AB = [
    [4+2, 0, 0, 0],
    [1+5, 0, 0, 0],
    [4+4, 0, 0, 0],
    [-1+6, 0, 0, 0]
]
your_answer_c_BA = [
    [4, 2, 1, -1],
    [4, 2, 1, -1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

your_answer_d_AB = [
    [0, 4+-1, 0, 4],
    [0, 1+3, 0, 1],
    [0, 4+0, 0, 4],
    [0, -1+-5, 0, -1]
]
your_answer_d_BA = [
    [1+-1, 5+6, -2+2, 3+-5],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 5, -2, 3]
]

your_answer_e_AB = [
    [0, -1*-3, 0, 4*2],
    [0, 3*-3, 0, 1*2],
    [0, 0*-3, 0, 4*2],
    [0, -5*-3, 0, -1*2]
]
your_answer_e_BA = [
    [2*-1, 2*6, 2*2, 2*-5],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [-3*1, -3*5, -3*-2, -3*3]
]

your_answer_f_AB = [
    [4*-1, 2*2, 1*2, -1*3],
    [1*-1, 5*2, -2*2, 3*3],
    [4*-1, 4*2, 4*2, 0*3],
    [-1*-1, 6*2, 2*2, -5*3]
]
your_answer_f_BA = [
    [-1*4, -1*2, -1*1, -1*-1],
    [2*1, 2*5, 2*-2, 2*3],
    [2*4, 2*4, 2*4, 2*0],
    [3*-1, 3*6, 3*2, 3*-5]
]



## 9: (Problem 4.17.11) Column-vector and row-vector matrix multiplication
column_row_vector_multiplication1 = Vec({0, 1}, {0:2*2+3*2+1*3, 1:1*2+3*2+4*3})

column_row_vector_multiplication2 = Vec({0, 1, 2}, {0:2*1+4*5+1*2, 1:2*2+4*1+1*3, 2:2*0+4*1+1*0})

column_row_vector_multiplication3 = Vec({0, 1, 2, 3}, {0:2*3+1*-2, 1:2*1+1*6, 2:2*5+1*1, 3:2*2+1*-1})

column_row_vector_multiplication4 = Vec({0,1}, {0:1*1+2*2+3*3+4*4, 1:1*1+1*2+3*3+1*4})

column_row_vector_multiplication5 = Vec({0, 1, 2}, {0:4*-1+1*1+-3*0, 1:4*1+1*0+-3*1, 2:4*1+1*2+-3*-1})


def lin_comb(clist, vlist):
    """
    Compute a linear combination
    :param clist: X len list of scalars
    :param vlist: X len list of vectors all of domain D
    :return: D domain vector whose values are summation of clist * vlist
    """
    return sum([s * v for s, v in zip(clist, vlist)])


# mat2rowdict, mat2coldict, rowdict2mat, coldict2mat


## 10: (Problem 4.17.13) Linear-combinations matrix-vector multiply
# You are also allowed to use the matutil module
def lin_comb_mat_vec_mult(M, v):
    '''
    Input:
      -M: a matrix
      -v: a vector
    Output: M*v
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    linear-combination definition of matrix-vector multiplication. 
    Examples:
    >>> M=Mat(({'a','b'},{'A','B'}), {('a','A'):7, ('a','B'):1, ('b','A'):-5, ('b','B'):2})
    >>> v=Vec({'A','B'},{'A':4, 'B':2})
    >>> lin_comb_mat_vec_mult(M,v) == Vec({'a', 'b'},{'a': 30, 'b': -16})
    True
    >>> M1=Mat(({'a','b'},{'A','B'}), {('a','A'):8, ('a','B'):2, ('b','A'):-2, ('b','B'):1})
    >>> v1=Vec({'A','B'},{'A':4,'B':3})
    >>> lin_comb_mat_vec_mult(M1,v1) == Vec({'a', 'b'},{'a': 38, 'b': -5})
    True
    '''
    assert(M.D[1] == v.D)
    clist = list()
    vlist = list()

    cols = mat2coldict(M)
    for key, col in cols.items():
        clist.append(v[key])
        vlist.append(col)


    return lin_comb(clist, vlist)


## 11: (Problem 4.17.14) Linear-combinations vector-matrix multiply
def lin_comb_vec_mat_mult(v, M):
    '''
    Input:
      -v: a vector
      -M: a matrix
    Output: v*M
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    linear-combination definition of vector-matrix multiplication.

    The only operation on "v" allowed is get the value via brackets (e.g. v[k]). Return a vector computed as a
    linear combination.

    Examples:
      >>> M=Mat(({'a','b'},{'A','B'}), {('a','A'):7, ('a','B'):1, ('b','A'):-5, ('b','B'):2})
      >>> v=Vec({'a','b'},{'a':2, 'b':-1})
      >>> lin_comb_vec_mat_mult(v,M) == Vec({'A', 'B'},{'A': 19, 'B': 0})
      True
      >>> M1=Mat(({'a','b'},{'A','B'}), {('a','A'):8, ('a','B'):2, ('b','A'):-2, ('b','B'):1})
      >>> v1=Vec({'a','b'},{'a':4,'b':3})
      >>> lin_comb_vec_mat_mult(v1,M1) == Vec({'A', 'B'},{'A': 26, 'B': 11})
      True
    '''
    assert(v.D == M.D[0])
    clist = list()
    vlist = list()

    rows = mat2rowdict(M)
    for key, row in rows.items():
        clist.append(v[key])
        vlist.append(row)

    return lin_comb(clist, vlist)

    pass

## 12: (Problem 4.17.15) dot-product matrix-vector multiply
# You are also allowed to use the matutil module
def dot_product_mat_vec_mult(M, v):
    '''
    Return the matrix-vector product M*v.
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    dot-product definition of matrix-vector multiplication. 
    Examples:
    >>> M=Mat(({'a','b'},{0,1}), {('a',0):7, ('a',1):1, ('b',0):-5, ('b',1):2})
    >>> v=Vec({0,1},{0:4, 1:2})
    >>> dot_product_mat_vec_mult(M,v) == Vec({'a', 'b'},{'a': 30, 'b': -16})
    True
    >>> M1=Mat(({'a','b'},{0,1}), {('a',0):8, ('a',1):2, ('b',0):-2, ('b',1):1})
    >>> v1=Vec({0,1},{0:4,1:3})
    >>> dot_product_mat_vec_mult(M1,v1) == Vec({'a', 'b'},{'a': 38, 'b': -5})
    True
    '''
    assert(M.D[1] == v.D)
    result = Vec(M.D[0], {})

    rows = mat2rowdict(M)
    for key, row in rows.items():
        result[key] = row * v

    return result



## 13: (Problem 4.17.16) Dot-product vector-matrix multiply
# You are also allowed to use the matutil module
def dot_product_vec_mat_mult(v, M):
    '''
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    dot-product definition of vector-matrix multiplication. 
    Examples:
      >>> M=Mat(({'a','b'},{0,1}), {('a',0):7, ('a',1):1, ('b',0):-5, ('b',1):2})
      >>> v=Vec({'a','b'},{'a':2, 'b':-1})
      >>> dot_product_vec_mat_mult(v,M) == Vec({0, 1},{0: 19, 1: 0})
      True
      >>> M1=Mat(({'a','b'},{0,1}), {('a',0):8, ('a',1):2, ('b',0):-2, ('b',1):1})
      >>> v1=Vec({'a','b'},{'a':4,'b':3})
      >>> dot_product_vec_mat_mult(v1,M1) == Vec({0, 1},{0: 26, 1: 11})
      True
      '''
    assert(v.D == M.D[0])
    result = Vec(M.D[1], {})

    cols = mat2coldict(M)
    for key, col in cols.items():
        result[key] = col * v

    return result



## 14: (Problem 4.17.17) Matrix-vector matrix-matrix multiply
# You are allowed to use the matutil module
def Mv_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    cols = dict()
    Bcols = mat2coldict(B)
    for key, Bcol in Bcols.items():
        cols[key] = A * Bcol
    return coldict2mat(cols)




## 15: (Problem 4.17.18) Vector-matrix matrix-matrix multiply
def vM_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    rows = dict()
    Arows = mat2rowdict(A)
    for key, Arow in Arows.items():
        rows[key] = Arow * B
    return rowdict2mat(rows)


def voting_record_agreement(data_file='UN_voting_data.txt'):
    """
    Compute the degree of agreement between countries. Note this calculate takes awhile for default data (~an hour)
    From there the data returned can be used to find agreement & disagreement between countries.

    M_sorted = sorted([(value,key) for key,value in M.f.items()])
    M_unique = {tuple(sorted(t[1])):t[0] for t in M_sorted}
    sorted([(value,key) for key, value in M_unique.items()])


    :param data_file: file in format "{country_name} vote0 vote1 vote2... voteN" per line
        where each vote is either 1 (yes), -1 (no) or 0 (abstain)
    :return: country x country Matrix with agreement score
    """
    lines = list(open(data_file))
    VnCs = coldict2mat({fields[0]:list2vec(list(map(int, fields[1:]))) for fields in [line.split() for line in lines]})
    return VnCs.transpose() * VnCs


## 16: (Problem 4.17.19) Comparing countries using dot-product
# Provide a set consisting of two strings
most_opposed_pair_of_countries = {'Belarus', 'United_States_of_America'} # -1927

# Provide a ten-element list of two-element sets of strings
most_opposed_10_pairs_of_countries = [
    ('Belarus', 'United_States_of_America'),
    ('Syria', 'United_States_of_America'),
    ('Cuba', 'United_States_of_America'),
    ('Algeria', 'United_States_of_America'),
    ('United_States_of_America', 'Viet_Nam'),
    ('Libya', 'United_States_of_America'),
    ('Guinea', 'United_States_of_America'),
    ('Mongolia', 'United_States_of_America'),
    ('Mali', 'United_States_of_America'),
    ('Sudan', 'United_States_of_America')
] # [t[1] for t in sorted([(value,key) for key, value in M_unique.items()])[0:10]]


# Provide a set consisting of two strings
most_agreeing_pair_of_countries = ('Philippines', 'Thailand') # [t[1] for t in sorted([(value,key) for key, value in M_unique.items()])][-1]


## 17: (Problem 4.17.20) Dictlist Helper
def dictlist_helper(dlist, k):
    '''
    Input: a list dlist of dictionaries which all have the same keys, and a key k
    Output: the list whose ith element is the value corresponding to the key k 
            in the ith dictionary of dlist
    Example:
    >>> dictlist_helper([{'apple':'Apfel','bread':'Brot'},{'apple':'manzana', 'bread':'pan'},{'apple':'pomme','bread':'pain'}], 'apple')
    ['Apfel', 'manzana', 'pomme']
    '''
    pass



## 18: (Problem 4.17.21) Solving 2x2 linear systems and finding matrix inverse
solving_systems_x1 = None
solving_systems_x2 = None
solving_systems_y1 = None
solving_systems_y2 = None
solving_systems_m = Mat(({0, 1}, {0, 1}), {...:...})
solving_systems_a = Mat(({0, 1}, {0, 1}), {...:...})
solving_systems_a_times_m = Mat(({0, 1}, {0, 1}), {...:...})
solving_systems_m_times_a = Mat(({0, 1}, {0, 1}), {...:...})



## 19: (Problem 4.17.22) Matrix inverse criterion
# Please write your solutions as booleans (True or False)

are_inverses1 = None
are_inverses2 = None
are_inverses3 = None
are_inverses4 = None

