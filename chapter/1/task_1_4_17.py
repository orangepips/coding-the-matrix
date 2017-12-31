from math import e, pi
from chapter.chapter1 import plot_with_pause

if __name__ == "__main__":

    n = 20

    w = e**(2 * pi * 1j / n)

    pts = [w**z for z in range(n)]

    print(pts)

    plot_with_pause(pts)
