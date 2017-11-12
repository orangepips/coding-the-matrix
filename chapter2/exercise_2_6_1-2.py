from chapter2.task_2_4_3 import add2, plot_with_pause
from chapter2.task_2_5_4 import scalar_vector_mult


def exercise_2_6_1():
    u = [2, 3]
    v = [5, 7]
    w = [3, 4] # (5, 7) - (2, 3) = (3, 4)
    translation_vector = u

    plot_with_pause([add2(scalar_vector_mult(i/100, w), u) for i in range(101)], 10)


def exercise_2_6_2(points=10):
    u = [1,4]
    v = [6,3]
    w = [5,-1]

    result = [add2(scalar_vector_mult(i/points, w), u) for i in range(points+1)]
    # print(result)
    plot_with_pause(result)

if __name__ == "__main__":
    exercise_2_6_1()
    exercise_2_6_2()

