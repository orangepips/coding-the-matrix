# Coding the Matrix: Resources

## Files

As linked from http://resources.codingthematrix.com/

### Python

 * [bitutil.py]
 * [cracking_rand.py]
 * [echelon.py]
 * [factoring_support.py]
 * [GF2.py]: Galois Field over 2
 * [image.py]
 * [image_mat_util.py]
 * [independence.py]
 * [mat.py]: contains the Mat class representing a matrix
 * [matutil.py] utilities for creating and manipulating matrices
 * [orthogonalization.py]
 * [plotting.py]
 * [png.py]
 * [solver.py]: solve the equation Ax = b as `x = solve(A, b)`
 * [triangular.py]
 * [vec.py]: contains the Vec class representing a Vector
 * [vecutil.py]: utilities for creating and manipulating vectors

### Images

 * [board.png]
 * [cit.png]
 * [head-paint.png]
 * [img01.png]

### Data Files

 * [UN_voting_data.txt]

## Decompiling pyc

I find the author's approach frustrating to include pyc inline within a .py file. Seems the only reason is to obscure from students.

In code such as [`solver.py`](solver.py) and [`independence.py`](independency.py)

 1. Install [`uncompyle6`](https://pypi.python.org/pypi/uncompyle6): $ `pip uncompyle6`
 1. Decode pyc string from base64 (e.g. `base64.decodebytes(pycData)`) and write to a file.
 1. From the command line execute `uncompyle6 -o . {pyc_file_name}.pyc` which will write a file `{pyc_file_name}.py`

See [`solver_write_pyc.py`](solver_write_pyc.py) for an example.