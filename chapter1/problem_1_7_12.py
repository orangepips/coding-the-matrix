from chapter1.task_1_4_11 import S, plot_with_pause
from math import e, pi


def transform(a, b, L): return [a * z + b for z in L]


if __name__ == "__main__":
    # TODO: read https://betterexplained.com/articles/understanding-why-complex-multiplication-works/
    # https://www2.clarku.edu/~djoyce/complex/mult.html > "Multiplication done algebraically."
    # (x + yi) (u + vi) = (xu - yv) + (xv + yu)i

    # Problem a.
    b1 = complex(1, 1)  # one unit up & one unit right
    a1 = 2 * e ** (pi/2 * 1j)  # rotate 90 degrees, scale by two
    s1_transformed = transform(a1, b1, S)
    plot_with_pause(S, 10)
    plot_with_pause(s1_transformed, 10)

    # Problem b.
    # Scale real part by two and imaginary part by three
    # rotate by 45 degrees CCW
    # traslate down 2 and left 3

    # don't believe problem b is solvable because there's no single complex
    # number to add or multiple each value in a list to scale the real and
    # imaginary part differently
