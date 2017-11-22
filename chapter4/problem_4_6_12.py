from collections import defaultdict
from operator import itemgetter
from mat import Mat


def find_triangle(M):
    """
    For the passed matrix M finds the row and column ordering, if it exists,
    of the triangular form. Recall a tuple can be unpacked as function arguments
    as function_name(*tuple_name)
    :param M: a matrix
    :return: a two tuple of lists ([rows], [columns]) in the triangular order OR None if none exists.
    >>> A = Mat(({'a', 'b', 'c'}, {'#', '@', '?'}),\
        {('a', '#'):2, ('a', '?'): 3,\
        ('b', '@'):10, ('b', '#'):20, ('b', '?'):30,\
        ('c', '#'): 35})
    >>> A_result = find_triangle(A)
    >>> A_result == (['b', 'a', 'c'], ['@', '?', '#'])
    True
    >>> B = Mat(({'a', 'b', 'c'}, {'#', '@', '?'}),\
        {('a', '#'):2, ('a', '?'): 3,\
        ('b', '@'):10, ('b', '#'):20, ('b', '?'):30,\
        ('c', '#'): 35, ('c', '?'): 11})
    >>> find_triangle(B) == None
    True
    """
    # TODO: there's probably a more pythonic way of doing this.
    zero_count = {'row': defaultdict(int), 'col': defaultdict(int)}

    [_increment_if_zero(M, pos, zero_count) for pos in [(r,c) for r in M.D[0] for c in M.D[1]]]
    row_tuples = sorted(zero_count['row'].items(), key=itemgetter(1))
    col_tuples = sorted(zero_count['col'].items(), key=itemgetter(1), reverse=True)

    rows = [r_t[0] for r_t_ix, r_t in enumerate(row_tuples) if r_t[1] == r_t_ix]
    cols = [c_t[0] for c_t_ix, c_t in enumerate(col_tuples) if c_t[1] == len(row_tuples) - c_t_ix - 1]

    return (rows, cols) if len(rows) == len(row_tuples) and len(cols) == len(col_tuples) else None


def _increment_if_zero(M, pos, zero_count):
    """
    :param M: matrix
    :param pos: 2 tuple (row, column)
    :param zero_count: dictionary of row and column zero counts
    :return: updated zero_count
    """
    # short circuit
    v = M[pos[0], pos[1]]

    zero_count['row'][pos[0]] += 1 if v == 0 else 0
    zero_count['col'][pos[1]] += 1 if v == 0 else 0

    return zero_count