# (a + b)u = au + bu
# a & b are vectors
# u is a scalar

def add_vectors(v1, v2): return [x + y for x, y in zip(v1, v2)]

def mult_vector_by_scalar(v, s): return [e * s for e in v]

if __name__ == "__main__":
    a = [1, 2]
    b = [3, 4]
    u = 5

    add_then_multiply = mult_vector_by_scalar(add_vectors(a, b), u)

    multiply_then_add = add_vectors(mult_vector_by_scalar(a, u), mult_vector_by_scalar(b, u))

    print(add_then_multiply, multiply_then_add)