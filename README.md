# coding-the-matrix

Coding work for the book from [http://codingthematrix.com/](http://codingthematrix.com/). 

While this does have some overlap with the Coursera course, the exercises tend to be more involved. 

Code written using Python 3.5.4 on OSX using the [Anaconda distribution](https://www.anaconda.com/download/). 

Each chapter's work is setup in a corresponding python package `chapter/#`

So to use you would type something like: 

    >>> from chapter.0 import dictutil
    >>> [dictutil.row(p, 20) for p in range(15)]

 * [Graded Stencil Files](grading/)
 * [Book Python Resources](resources/)

# Comments

 * `itertools` has been useful for many different problems
 * Given all the issues with floating point arithmetic, should use the [`Decimal`](https://docs.python.org/3/library/decimal.html) module instead.
 * Sections entitled **Problem X.Y.Z** are exercises for the reader.
 * **Problem 2.14.10** the `Vec` class should be implemented earlier in the chapter. 
 * **Problem 4.17.12** the `Mat` class should be implemented earlier in the chapter. 
 * [`solver.py`](solver.py) module implementation is based 64 encoded pyc. No comments explaining why. 
 * 5.11 The Exchange Lemma is not well explained. It could use a concrete example before Problem 5.14.11
 * 9.2.2 Augmenting `project_orthogonal` goes way off the reservation:
   * The Mathese vs Python array indexing syntax of one versus zero, respectively is annoying. That this section announces the Mathese therein will use zero is simply maddening.
   * Then telling the reader about what's Pythonic or not, is even nuttier.

# Kindle Version Bugs

 * OSX copy paste is a clown show.
   * Never clear when it's possible to copy or not.
   * Copying includes the copy right text.
 * Missing Images
   * p 484
   * p 499-500 Fourier Transformations & Charting Waves
   


# Errors Found

All of the following have also been sent to `info@codingthematrix.com`

A ^ at the end of a line indicates a "confirmed" response.  

 * [2.9.15](chapter2/quiz_2_9_15_errata.py) Off By One^ 
 * 4.9.3 XKCD Matrix Transform should reference https://xkcd.com/184/ not https://xkcd.com/824/ ^
 * [`ecc_lab.py`](./matrix/ecc_lab.py) Task 10 Bug: passes doctest but fails via `submit.py` ^
 * `matrix_resources/images`: Section 4.15.5 references but not on the web site. Checked: 
   * http://resources.codingthematrix.com/ 
   * http://grading.codingthematrix.com/edition1/index.html
   * http://resources.codingthematrix.com/images/
   * http://resources.codingthematrix.com/matrix_resources/images/
 * [`geometry_lab.py`](matrix/geometry_lab.py) Task 4 (Line 59) missing lead doctest angle brackets ">>>"
 * [`The_Matrix_Problems.py`](matrix/The_Matrix_problems.py) Problem 16's `most_agreeing_pair_of_countries` is marked incorrect
 * Problem 5.14.9 (c) not answerable due to value of last vector being cutoff (Kindle edition). Copy and paste doesn't solve as it comes across as:
   ```
   [one, one, 0, one, one], [0, 0, one, 0, 0], [0, 0, one, one, one], [one, 0, one, one, one], [one, one, one,
   
   Problem 5.14.10: Each of the subproblems...
   ```
 * `submit.py` grading for Problem 7.9.7 in [`Gaussian_Eliminating_problems.py`](grading/Gaussian_Elimination_problems.py) expects `row_list` but has `rowlist`.
 * `submit.py` grading for Problem 8.6.3 #2 in [`The_Inner_Product_problems.py`](grading/The_Inner_Product_problems.py) does not adhere to the description of 6 decimal places allowed where `project_along(b, v)` and `project_orthogonal_1(b, v)` produce decimals that I in turn rounded. Instead it wants vector values to fractions (`x/y`).
 * http://resources.codingthematrix.com/orthonormalization.py update doctests to match http://grading.codingthematrix.com/edition1/Orthogonalization_problems.py