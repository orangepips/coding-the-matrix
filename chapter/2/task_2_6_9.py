from chapter.chapter1 import plot_with_pause
from chapter2.problem_2_6_6 import add_vectors, mult_vector_by_scalar


def segment(pt1, pt2, points = 100):
    return [add_vectors(mult_vector_by_scalar(pt1, a/points), mult_vector_by_scalar(pt2, b/points))
            for a, b in zip(range(points, -1, -1), range(points+1))]

if __name__ == "__main__":
    pt1 = [3.5, 3]
    pt2 = [0.5, 1]

    plot_with_pause(segment(pt1, pt2, 50), 4, 1)