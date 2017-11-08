from math import e, pi
from chapter1.task_1_4_11 import S, plot_with_pause

def rotate(c_nums, radians=pi/4):
    return [c * e ** (radians * 1j) for c in c_nums]

if __name__ == "__main__":
    S_rotated = rotate(S, pi/4)

    print(S_rotated)
    plot_with_pause(S_rotated, 5)