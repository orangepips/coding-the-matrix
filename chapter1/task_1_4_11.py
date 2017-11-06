from chapter1.plotting import plot
#from chapter1.image import file2image

S = {2+2j, 3+2j, 1.75 + 1j, 2+1j, 2.25 + 1j, 2.5+1j, 2.75 + 1j, 3+1j, 3.25 + 1j}

def f(z):
    pass

def find_boundaries(cmplx_nums):
    min_boudary = None
    max_boundary = None

    for n in cmplx_nums:
        if min_boudary is None: min_boudary = n
        if max_boundary is None: max_boundary = n

        if n.real > max_boundary.real: max_boundary = complex(n.real, max_boundary.imag)
        elif n.real < min_boudary.real: min_boudary = complex(n.real, min_boudary.imag)

        if n.imag > max_boundary.imag: max_boundary = complex(max_boundary.real, n.imag)
        elif n.imag < min_boudary.imag: min_boudary = complex(min_boudary.real, n.imag)

        '''
        print("n:\t" + str(n))
        print(min_boudary)
        print(max_boundary)
        '''

    return (min_boudary, max_boundary)

def plot_centered(cmplx_nums, min_boundary, max_boundary):
    delta = max_boundary - min_boundary

    plot({n - (min_boundary + delta / 2) for n in cmplx_nums})
    input("Press Enter to continue...")

if __name__ == "__main__":
    min_boundary, max_boundary = find_boundaries(S)
    plot_centered(S, min_boundary, max_boundary)
