from plotting import plot

S = {2+2j, 3+2j, 1.75 + 1j, 2+1j, 2.25 + 1j, 2.5+1j, 2.75 + 1j, 3+1j, 3.25 + 1j}


def find_boundaries(cmplx_nums):
    min_boudary = None
    max_boundary = None

    for n in cmplx_nums:
        if min_boudary is None:
            min_boudary = n
        if max_boundary is None:
            max_boundary = n

        if n.real > max_boundary.real:
            max_boundary = complex(n.real, max_boundary.imag)
        elif n.real < min_boudary.real:
            min_boudary = complex(n.real, min_boudary.imag)

        if n.imag > max_boundary.imag:
            max_boundary = complex(max_boundary.real, n.imag)
        elif n.imag < min_boudary.imag:
            min_boudary = complex(min_boudary.real, n.imag)

        '''
        print("n:\t" + str(n))
        print(min_boudary)
        print(max_boundary)
        '''

    return min_boudary, max_boundary


def center(cmplx_nums):
    min_boundary, max_boundary = find_boundaries(cmplx_nums)
    delta = max_boundary - min_boundary
    return {n - (min_boundary + delta / 2) for n in cmplx_nums}, delta


def plot_centered(cmplx_nums, print_scale=False):
    cmplx_nums_centered, delta = center(cmplx_nums)
    scale = max(delta.real, delta.imag)
    if print_scale:
        print(scale)
    plot_with_pause(cmplx_nums_centered, scale)


def plot_with_pause(pts, scale=5, dot_size=2):
    plot(pts, scale, dot_size)
    # pause otherwise the temp file generated is deleted before it can displayed
    input("Press Enter to continue...")


if __name__ == "__main__":
    plot_centered(S)
