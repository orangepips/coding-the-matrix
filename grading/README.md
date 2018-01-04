From http://grading.codingthematrix.com/edition1/index.html

# Coding the Matrix: By Chapter Graded Python Files

Most of these are meant to be run through [submit.py](submit.py). All are completed versions of stencils downloaded from http://grading.codingthematrix.com/edition1/index.html

Note, [submit.py](submit.py) does not create a `receipt` directory or capture submission results in a file.

**Chapter 2: The Vector**

 * [The_Vector_problems.py]
 * [politics_lab.py]
 * [../resources/vec.py]

**Chapter 3: The Vector Space**

 * [The_Vector_Space_problems.py]

**Chapter 4: The Matrix**

 * [The_Matrix_problems.py]
 * [ecc_lab.py]
 * [geometry_lab.py]
 * [../resources/mat.py]

**Chapter 5: The Basis**

 * [The_Basis_problems.py]
 * [perspective_lab.py]

**Chapter 6: Dimension**

 * [Dimension_problems.py]

**Chapter 7: Guassian Elimination**

 * [secret_sharing_lab.py]
 * [factoring_lab.py]
 * [Guassian_Elimination_problems.py]

**Chapter 8: The Inner Product**

 * [machine_learning_lab.py]
 * [The_Inner_Product_problems.py]

# Auto-grading for Coding the Matrix, Edition One (beta version)

Make sure you have Python 3.x on your computer.  In the following, I will assume that python3 is the command used to invoke Python.  (On Windows, it might be just python.)

Create a single directory, called matrix, in which you will put all your code.

Download the submission script, submit.py, to the matrix directory.

To get your work graded, 

 * download the appropriate stencil file into the matrix directory,
 * edit it to include answers to whichever problems you choose,
 * make sure you can import it into Python without error,
 * test your solutions, and
 * finally submit problems from a given stencil by using the following command from a console or shell or Command Prompt:

`python3 submit.py <stencil filename>`

For example, to submit solutions to problems appearing in the chapter The Function, edit The_Function.py, and then use the command

`python3 submit.py The_Function.py`

Note that these commands are executed not from within the Python REPL, but within a console or shell or Command Prompt.

## More about submit

The submit script asks for your username. This can be anything you like. When you submit a correct answer, the script stores a "receipt" in a subdirectory receipts of your `matrix` directory, specifying your username, the data, and the identifier of the problem you solved. 

To avoid having to give your username each time you run the submit script, you can create a file `profile.txt` in your `matrix` directory with the following line in it:

`USERNAME philipklein` 

where "philipklein" is replaced with your chosen username. Later I will write about other features of the submit script. In particular, we plan to have a leaderboard; you will be able to request that your successful submits be reported to the leaderboard.

## The Stencil files

More stencil files will be added as I complete them.  Note that these are still rough and should be considered beta versions.  Contact me at info@codingthematrix.com if you have questions or bug reports. 