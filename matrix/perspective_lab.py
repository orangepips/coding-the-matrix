# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from mat import Mat
from matutil import rowdict2mat, mat2coldict, coldict2mat
from itertools import chain
from solver import solve
import image_mat_util


## 1: (Task 5.12.1) Move To Board
def move2board(y): 
    """
    Whiteboard coordinate representation of q (y1, y2, y3)
    Whiteboard coordinate representation of point p is (y1/y3, y2/y3, y3/3). Meaning 3rd coordinate is 1.
    :param y: {'y1', 'y2', 'y3'} vector, coordinate representation in whiteboard coordinates of a point q
    :return: {'y1', 'y2', 'y3'} vector, coordinate represenation in whiteboard coordinates of a point p such that
        the line through the origin and q intersects the whiteboard plane at p

    >>> D = {'y1', 'y2', 'y3'}
    >>> move2board(Vec(D, {'y1': 2, 'y2': 3, 'y3': 4})) == Vec(D, {'y1': 2/4, 'y2': 3/4, 'y3': 4/4})
    True
    """
    y1 = y['y1']
    y2 = y['y2']
    y3 = y['y3']
    # print(y1, y2, y3)
    # return Vec(y.D, {})
    return Vec(y.D, {'y1': y1/y3, 'y2': y2/y3, 'y3': y3/y3})



## 2: () Make domain of vector
# D should be assigned the Cartesian product of R and C
D = {(y, x) for y in ['y1', 'y2', 'y3'] for x in ['x1', 'x2', 'x3']}


## 3: (Task 5.12.2) Make Equations
def make_equations(x1, x2, w1, w2): 
    '''
    Input:
        - x1, x2: pixel coordinates of a point q in the image plane
        - w1, w2: w1=y1/y3 and w2=y2/y3 where y1,y2,y3 are the whiteboard coordinates of q.
    Output:
        - List [u,v] of D-vectors that define linear equations u*h = 0 and v*h = 0

    For example, suppose we have an image of the whiteboard in which
       the top-left (0,0,1) whiteboard corner appears at pixel coordinates 9, 18
       the bottom-left (0,1,1) whiteboard corner appears at pixel coordinates 8,25
       the top-right (1,0,1) whiteboard corner appears at pixel coordinates 20,20
       the bottom-right (1,1,1) whiteboard corner appears at pixel coordinates 18,23

    Let q be the point in the image plane with pixel coordinates x=8,y=25, i.e. camera coordinates (8,25,1).
    Let y1,y2,y3 be the whiteboard coordinates of the same point.  The line that goes through the
    origin and p intersects the whiteboard at a point p.  That point p is the bottom-left corner of
    the whiteboard, so its whiteboard coordinates are 0,1,1.  Therefore (y1/y3,y2/y3,y3/y3) = (0,1,1).
    We define w1=y1/y3 and w2=y2/y3, so w1 = 0 and w2 = 1.  Given this input-output pair, let's find
    two linear equations u*h=0 and v*h=0 constraining the unknown vector h whose entries are the entries
    of the matrix H. 

    >>> for v in make_equations(8,25,1,0): print(v)
    <BLANKLINE>
     ('y1', 'x1') ('y1', 'x2') ('y1', 'x3') ('y2', 'x1') ('y2', 'x2') ('y2', 'x3') ('y3', 'x1') ('y3', 'x2') ('y3', 'x3')
    ---------------------------------------------------------------------------------------------------------------------
               -8          -25           -1            0            0            0            8           25            1
    <BLANKLINE>
     ('y1', 'x1') ('y1', 'x2') ('y1', 'x3') ('y2', 'x1') ('y2', 'x2') ('y2', 'x3') ('y3', 'x1') ('y3', 'x2') ('y3', 'x3')
    ---------------------------------------------------------------------------------------------------------------------
                0            0            0           -8          -25           -1            0            0            0

    Note that the negations of these vectors form an equally valid solution.

    Similarly, consider the point q in the image plane with pixel coordinates 18, 23.  Let y1,y2,y3 be the whiteboard
    coordinates of p.  The corresponding point p in the whiteboard plane is the bottom-right corner, and the whiteboard
    coordinates of p are 1,1,1, so (y1/y3,y2/y3,y3/y3)=(1,1,1).  We define w1=y1/y3 and w2=y2/y3, so w1=1 and w2=1.
    We obtain the vectors u and v defining equations u*h=0 and v*h=0 as follows:

    >>> for v in make_equations(18,23,1,1): print(v)
    <BLANKLINE>
     ('y1', 'x1') ('y1', 'x2') ('y1', 'x3') ('y2', 'x1') ('y2', 'x2') ('y2', 'x3') ('y3', 'x1') ('y3', 'x2') ('y3', 'x3')
    ---------------------------------------------------------------------------------------------------------------------
              -18          -23           -1            0            0            0           18           23            1
    <BLANKLINE>
     ('y1', 'x1') ('y1', 'x2') ('y1', 'x3') ('y2', 'x1') ('y2', 'x2') ('y2', 'x3') ('y3', 'x1') ('y3', 'x2') ('y3', 'x3')
    ---------------------------------------------------------------------------------------------------------------------
                0            0            0          -18          -23           -1           18           23            1

    Again, the negations of these vectors form an equally valid solution.
    '''
    u = Vec(D, {
        ('y3', 'x1'): w1 * x1, ('y3', 'x2'): w1 * x2, ('y3', 'x3'): w1, ('y1', 'x1'): -x1, ('y1', 'x2'): -x2, ('y1', 'x3'): -1
    })
    v = Vec(D,{
        ('y3', 'x1'): w2 * x1, ('y3', 'x2'): w2 * x2, ('y3', 'x3'): w2, ('y2', 'x1'): -x1, ('y2', 'x2'): -x2, ('y2', 'x3'): -1
    })
    return [u, v]



## 4: () Scaling row
# This is the vector defining the scaling equation
w = Vec(D, {('y1', 'x1'): 1})



## 5: () Right-hand side
# Now construct the Vec b that serves as the right-hand side for the matrix-vector equation L*hvec=b
# This is the {0, ..., 8}-Vec whose entries are all zero except for a 1 in position 8
b = Vec(set(range(9)), {8:1})

pixel_corners = [(358, 36), (329, 597), (592, 157), (580, 483)] # for board.png

## 6: () Rows of constraint matrix
def make_nine_equations(corners):
    '''
    input: a list of four tuples:
           [(i0,j0),(i1,j1),(i2,j2),(i3,j3)]
           where i0,j0 are the pixel coordinates of the top-left corner,
                 i1,j1 are the pixel coordinates of the bottom-left corner,
                 i2,j2 are the pixel coordinates of the top-right corner,
                 i3,j3 are the pixel coordinates of the bottom-right corner,
    output: the list of Vecs u0, u1, ..., u8 that are to be the rows of the matrix.
    Vecs u0,u1 come from applying make_equations to the top-left corner,
    Vecs u2,u3 come from applying make_equations to the bottom-left corner,
    Vecs u4,u5 come from applying make_equations to the top-right corner,
    Vecs u6,u7 come from applying make_equations to the bottom-right corner,
    Vec u8 is the vector w.

    top left x1 = 358, x2 = 36
    bottom left x1 = 329, x2 = 597
    top right x1 = 592, x2 = 157
    bottom right x1 = 580, x2 = 483
    >>> equations = make_nine_equations(pixel_corners)
    >>> len(equations) == 9
    True
    >>> equations[8] == w
    True
    >>> print(equations)
    '''
    top_left = (0, 0)
    bottom_left = (0, 1)
    top_right = (1, 0)
    bottom_right = (1, 1)
    whiteboard_corners = [top_left, bottom_left, top_right, bottom_right]
    result = list(chain.from_iterable([make_equations(*pixels, *whiteboard) for pixels, whiteboard in zip(corners, whiteboard_corners)]))
    result.append(w)
    return result



## 7: (Task 5.12.4) Build linear system
# Apply make_nine_equations to the list of tuples specifying the pixel coordinates of the
# whiteboard corners in the image.  Assign the resulting list of nine vectors to veclist:
veclist = make_nine_equations(pixel_corners)

# Build a Mat whose rows are the Vecs in veclist
L = Mat((b.D, w.D), {(row, col): veclist[row][col] for row in b.D for col in w.D})



## 8: () Solve linear system
# Now solve the matrix-vector equation to get a Vec hvec, and turn it into a matrix H.
hvec = solve(L, b) # had look here https://github.com/franzip/coursera/blob/master/coding-the-matrix/week5/perspective_lab.py#L140
H = Mat(({'y1', 'y2', 'y3'}, {'x1', 'x2', 'x3'}), {(key[0], key[1]):hvec[key] for key in hvec.D})
# print(H)

# Task 5.12.5
# (X_pts, colors) = image_mat_util.file2mat('board.png', ('x1','x2','x3'))
# Task 5.12.6
# Y_pts = H * X_pts

## 9: (Task 5.12.7) Y Board Comprehension
def mat_move2board(Y):
    '''
    Input:
        - Y: a Mat each column of which is a {'y1', 'y2', 'y3'}-Vec
          giving the whiteboard coordinates of a point q.
    Output:
        - a Mat each column of which is the corresponding point in the
          whiteboard plane (the point of intersection with the whiteboard plane 
          of the line through the origin and q).

    Example:
    >>> Y_in = Mat(({'y1', 'y2', 'y3'}, {0,1,2,3}),
    ...     {('y1',0):2, ('y2',0):4, ('y3',0):8,
    ...      ('y1',1):10, ('y2',1):5, ('y3',1):5,
    ...      ('y1',2):4, ('y2',2):25, ('y3',2):2,
    ...      ('y1',3):5, ('y2',3):10, ('y3',3):4})
    >>> print(Y_in)
    <BLANKLINE>
            0  1  2  3
          ------------
     y1  |  2 10  4  5
     y2  |  4  5 25 10
     y3  |  8  5  2  4
    <BLANKLINE>
    >>> print(mat_move2board(Y_in))
    <BLANKLINE>
               0 1    2    3
          ------------------
     y1  |  0.25 2    2 1.25
     y2  |   0.5 1 12.5  2.5
     y3  |     1 1    1    1
    <BLANKLINE>
    '''
    return coldict2mat({key:move2board(col) for key, col in mat2coldict(Y).items()})


def change_perspective(img_path, cp_pixel_corners=pixel_corners, scale=100):
    cp_veclist = make_nine_equations(cp_pixel_corners)
    cp_L = Mat((b.D, w.D), {(row, col): cp_veclist[row][col] for row in b.D for col in w.D})
    cp_hvec = solve(cp_L, b)
    cp_H = Mat(({'y1', 'y2', 'y3'}, {'x1', 'x2', 'x3'}), {(key[0], key[1]):cp_hvec[key] for key in cp_hvec.D})

    (X_pts, colors) = image_mat_util.file2mat(img_path, ('x1', 'x2', 'x3'))
    Y_board = mat_move2board(cp_H * X_pts)
    image_mat_util.mat2display(Y_board, colors, ('y1', 'y2', 'y3'), scale=scale, xmin=None, ymin=None)

# In Mac Preview select a point and drag to the upper left hand corner to get pixel measurements.
# top left, bottom left, top right, bottom right

# TODO: figure out a good way to determine scale value

# this gives a pretty good result for cit.png
# change_perspective('cit.png', rb_pixel_corners=[(83, 74), (82, 103), (106, 69), (105, 102)], scale=25)
