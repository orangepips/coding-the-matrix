# coding-the-matrix

Coding work for the book from [http://codingthematrix.com/](http://codingthematrix.com/). 

While this does have some overlap with the Coursera course, the exercises tend to be more involved. 

Code written using Python 3.5.4 on OSX using the [Anaconda distribution](https://www.anaconda.com/download/). 

Each chapter's work is setup in a corresponding python package `chapter#`

So to use you would type something like: 

    >>> from chapter0 import dictutil
    >>> [dictutil.row(p, 20) for p in range(15)]   
    
# Comments 

 * **Problem 2.14.10** the `Vec` class should be implemented earlier in the chapter. 
 * **Problem 4.17.12** the `Mat` class should be implemented earlier in the chapter. 
 * [`solver.py`](solver.py) module implementation is based 64 encoded pyc. No comments explaining why. 

# Errors Found

All of the following have also been sent to info@codingthematrix.com

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

 
