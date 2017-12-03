from matutil import listlist2mat
from vecutil import list2vec

def mul(A, B):
    """
    Multiply A * B
    :param A: J x K matrix
    :param B: K x L matrix
    :return: J x L matrix

    >>> listlist2mat([[2,3],[4,2]]) * listlist2mat([[1,2],[2,3]]) == listlist2mat([[],[]])
    """