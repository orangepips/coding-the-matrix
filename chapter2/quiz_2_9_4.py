"""
u, v equal length lists
return dot product
"""
def list_dot(u, v):
    """
    :param u: X len list of elements
    :param v: X len list of elements
    :return: dot product (i.e. sum) of u and v interpreted as vectors
    """
    return sum([a * b for (a, b) in zip(u, v)])