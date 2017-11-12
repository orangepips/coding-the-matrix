"""
u, v equal length lists
return dot product
"""
def list_dot(u, v):
    return sum([a * b for (a, b) in zip(u, v)])