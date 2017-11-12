from chapter2.task_2_4_2 import L
from chapter1.task_1_4_11 import plot_with_pause

def add2(v, w): return [v[0]+w[0], v[1]+w[1]]

if __name__ == "__main__":
    plot_with_pause([add2(v, [1,2]) for v in L], 4)
