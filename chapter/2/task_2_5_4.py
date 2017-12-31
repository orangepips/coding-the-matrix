from chapter2.task_2_4_2 import L, plot_with_pause

def scalar_vector_mult(alpha, v): return [alpha * v[i] for i in range(len(v))]

if __name__ == "__main__":
    plot_with_pause([scalar_vector_mult(.5, e) for e in L])
    plot_with_pause([scalar_vector_mult(-.5, e) for e in L])