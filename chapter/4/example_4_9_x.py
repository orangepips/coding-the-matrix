from resources.matutil import identity, mat2rowdict
from resources.vecutil import list2vec
from math import sin, cos, radians

G2 = identity({0, 1}, 1)
G2r = mat2rowdict(G2)

a = 2

def _derive(M, coords):
    return M * coords

def example_4_9_3(coords):
    """
    Scale the x coordinate by 2
    :param coords: 2-vector coordinates x, y
    :return: vector scaled by 2

    >>> example_4_9_3(G2r[0]) == list2vec([2, 0])
    True
    >>> example_4_9_3(G2r[1]) == list2vec([0, 1])
    True
    """
    #return _derive(listlist2mat([[2, 0], [0, 1]]), coords)
    return list2vec([2*coords[0], coords[1]])

def example_4_9_4(coords):
    """
    Rotate points in 2D by 90 degrees (x, y) -> (-y, x) CCW
    :param coords: 2-vector coordinates x, y
    :return: vector rotated by 90 degrees

    >>> example_4_9_4(G2r[0]) == list2vec([0, 1])
    True
    >>> example_4_9_4(G2r[1]) == list2vec([-1, 0])
    True
    """
    #return _derive(listlist2mat([[0, -1], [1, 0]]), coords)
    return list2vec([-coords[1], coords[0]])

def example_4_9_5(coords, theta=30):
    """
    Rotate coordinates around the origin counter clockwise by theta
    :param coords: 2-vector coordinates x, y
    :param theta: degrees to rotate coords by counterclockwise
    :return: vector rotated by theta counterclockwise

    >>> theta = 30
    >>> theta_r = radians(theta)
    >>> L = example_4_9_5(G2r[0], theta)
    >>> R = list2vec([cos(theta_r), sin(theta_r)])
    >>> L == R
    True
    >>> example_4_9_5(G2r[1], theta) == list2vec([-sin(theta_r), cos(theta_r)])
    True
    """
    theta = radians(theta)
    #return _derive(listlist2mat([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]]), coords)
    # https://matthew-brett.github.io/teaching/rotation_2d.html
    x1 = coords[0]
    y1 = coords[1]
    x2 = x1 * cos(theta) - y1 * sin(theta)
    y2 = x1 * sin(theta) + y1 * cos(theta)
    return list2vec([x2, y2])


def example_4_9_6(coords):
    """
    Translate two units up an one right
    :param coords: 2-vector coordinates x, y
    :return: vector translated

    >>> example_4_9_6(G2r[0]) == list2vec([2, 2])
    True
    >>> example_4_9_6(G2r[1]) == list2vec([1, 3])
    True
    """
    #return _derive(listlist2mat([[2, 1], [2, 3]]), coords)
    return list2vec([coords[0] + 1, coords[1] + 2])