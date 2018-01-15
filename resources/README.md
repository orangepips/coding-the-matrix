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
 * ^[independence.py]: `rank(list_of_vectors)`, `is_independent(list_of_vectors)`
 * [mat.py]: contains the Mat class representing a matrix
 * [matutil.py] utilities for creating and manipulating matrices
 * [orthogonalization.py]
 * [plotting.py]
 * [png.py]
 * ^[solver.py]: solve the equation Ax = b as `x = solve(A, b)`
 * [triangular.py]
 * [vec.py]: contains the Vec class representing a Vector
 * [vecutil.py]: utilities for creating and manipulating vectors

^ indicates file contains pyc byte code.

### Images

 * [images/board.png]
 * [images/cit.png]
 * [images/Dali.png]: provided for Chapter 10 wavelet lab (dimensions are power of 2)
 * [images/flag.png]: provided for Chapter 10 wavelet lab (dimensions are power of 2)
 * [images/head-paint.png]
 * [images/img01.png]

### Data Files

 * [data/age-height.txt]
 * [data/train.data]
 * [data/UN_voting_data.txt]
 * [data/validate.data]


## Decompiling pyc

**Note, both approaches are unable to decompile `solver.py` and `independence.py` completely.**

I find the author's approach frustrating to include pyc inline within a .py file. Seems the only reason is to obscure from students.

Use Python 3.4 as decompilers work best with it. In code such as [`solver.py`](solver.py) and [`independence.py`](independency.py)

 1. Install both:
   1. [`uncompyle6`](https://pypi.python.org/pypi/uncompyle6): $ `pip uncompyle6`
   1. Install [`Decompyle++`](https://github.com/zrax/pycdc)
 1. Decode pyc string from base64 (e.g. `base64.decodebytes(pycData)`) and write to a file.
 1. From the command line execute
    1. `uncompyle6 -o . {pyc_file_name}.pyc` which will write a file `{pyc_file_name}.py` OR
    1. `./pycdc {pyc_file_name}.pyc`

See [`solver_write_pyc.py`](solver_write_pyc.py) for an example.

## `__init__.py` Solve for `resources` Module

[__init__.py] is modified to alias several modules in this directory. For example `resources.GF2` as `GF2`.

This was done to support `independence.py` and `solver.py` `import` statements within their embedded pyc.