from chapter2.task_2_5_4 import scalar_vector_mult
from chapter2.quiz_2_9_4 import list_dot
from chapter2.task_2_4_3 import add2


'''
2.9.23 Homogenity of the dot-product

a scalar
u, v lists

(a * u) * v == a (u * v)
'''
def problem_2_9_23(a, u, v):
    left = list_dot(scalar_vector_mult(a, u), v)
    right = a * list_dot(u, v)
    return format_output("2.9.23", left, right)

"""
2.9.24 Not Always True  

a scalar
u, v lists 

(au) * (av) == a (u*v)
"""
def problem_2_9_24(a, u, v):
    left = list_dot(scalar_vector_mult(a, u), scalar_vector_mult(a, v))
    right = a * list_dot(u, v)
    return format_output("2.9.24", left, right)

"""
2.9.26 

u, v, w lists

Demonstrate false

(u + v) * (w+v) == u*w + v*w

"""
def problem_2_9_26(u, v, w):
    left = list_dot(add2(u, v), add2(w, v))
    right = list_dot(u, w) + list_dot(v, w)
    return format_output("2.9.26", left, right)

def format_output(problem, left, right):
    return "{0}\nLeft:\t{1}\nRight:\t{2}\nEqual:\t{3}".format(problem, left, right, left == right)


if __name__ == "__main__":
    a = 3
    u = [1, 2, 3]
    v = [4, 5, 6]
    w = [7, 8, 9]

    print(problem_2_9_23(a, u, v))
    print(problem_2_9_24(a, u, v))
    print(problem_2_9_26(u, v, w))