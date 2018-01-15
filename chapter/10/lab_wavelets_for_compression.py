from resources.vec import Vec

# Code assumes power of two representations. To adapt for other respresentations pad with zeroes.

# task 10.9.1
def forward_no_normalization(v):
    """
    :param v: list representing a vector in Rn where n is some power of 2
    :return: a dictionary giving the representation of the input vector in terms of the unnormalized Haar wavelet
    basis. The key for the coefficient of w j/i should be the tuple(j, i)
    >>> expected1 = \
        { \
            (2, 1): -1, (2, 0): -1, \
            (1, 0): -2.0, \
            (0, 0): 2.5 \
        }
    >>> forward_no_normalization([1, 2, 3, 4]) == expected1
    True
    >>> expected2 = \
     { \
        (8,7): 0, (8,6): 0, (8,5): -2, (8,4): 2, (8,3): -1, (8,2): -1, (8,1): -4, (8,0): -1, \
        (4,3): 0.0, (4,2): 4.0, (4,1): 2.0, (4,0): -0.5, \
        (2,1): 6.0, (2,0): 1.25, \
        (1,0): 1.125, \
        (0,0): 3.5625 \
    }
    >>> v=[4,5,3,7,4,5,2,3,9,7,3,5,0,0,0,0]
    >>> forward_no_normalization(v) == expected2
    True
    >>> similarity_between_nearby_pixels = [1, 1, 2, 2]
    >>> forward_no_normalization(similarity_between_nearby_pixels)
    {(2, 0): 0, (1, 0): -1.0, (0, 0): 1.5, (2, 1): 0}
    >>> nearby_pixels_vary_wildly = [0, 1, 1, 1, -1, 1, 0, 1, 100, 101, 102, 100, 101, 100, 99, 100]
    >>> forward_no_normalization(nearby_pixels_vary_wildly)
    {(8, 3): -1, (0, 0): 50.4375, (8, 2): -2, (8, 1): 0, (4, 1): -0.5, (4, 3): 1.0, (8, 0): -1, (2, 1): 0.75, (2, 0): 0.5, (8, 7): -1, (4, 2): -0.5, (8, 6): 1, (1, 0): -99.875, (4, 0): -0.5, (8, 5): 2, (8, 4): -1}
    """
    D = {}
    while len(v) > 1:
        k = len(v)
        # v is a k-element list
        vnew = [ (v[2*i] + v[2*i+1])/2 for i in range(k//2) ] # compute downsample 1-d image of size k//2 from v
        # vnew is a k//2-element list
        w = [ (v[2*i] - v[2*i+1]) for i in range(k//2) ] # computer unnormalized coeffients of basis for W(k/2)
        # w is a list of coefficients
        D.update({(k//2, i): w[i] for i in range(k//2)}) # dictionary with keys (k//2, 0), (k//2, 1) ..., (k//2, k//2-1) and values from w

        v = vnew
    # v is a 1-element list
    D[(0, 0)] = v[0] # store the last coefficient
    return D


# task 10.9.2
def normalize_coefficients(n, D):
    """
    :param n: integer dimension of the original space
    :param D: dictionary in the form returned by forward_no_normalization(v):
    :return: corresponding dictionary with the coefficients noramlized
    >>> expected = {(2, 0): -0.7071067811865476, (0, 0): 5.0, (1, 0): -2.0, (2, 1): -0.7071067811865476}
    >>> Dexpected = \
        { \
            (2, 1): -1, (2, 0): -1, \
            (1, 0): -2.0, \
            (0, 0): 2.5 \
        }
    >>> D = forward_no_normalization([1,2,3,4])
    >>> normalize_coefficients(len(list(D.keys())), D) == expected
    True
    >>> D == Dexpected
    True
    """
    wold = n
    Dc = D.copy()
    while True:
        w = wold//2
        sq_norm = (n / (4 * w))**(1/2) if w > 0 else n**(1/2)
        if w == 0:
            Dc[0, 0] = Dc[0, 0] * sq_norm
            break
        Dc.update({(w, i): Dc[(w, i)] * sq_norm for i in range(w)})
        wold = w
    return Dc


# task 10.9.3
def forward(v):
    """
    Find the representation with respect to the normalized Haar wavelet basis
    :param v: list representing a vector in Rn where n is some power of 2
    :return: combination of forward_no_normalization(v) and normalize_coefficients(n, D)
    >>> expected = {(2, 0): -0.7071067811865476, (0, 0): 5.0, (1, 0): -2.0, (2, 1): -0.7071067811865476}
    >>> forward([1, 2, 3, 4]) == expected
    True
    """
    n = len(v)
    return normalize_coefficients(n, forward_no_normalization(v))


# task 10.9.4
def suppress(D, threshold):
    """
    :param D: representation of the vector with respect to the normalized basis
    :param threshold: test value
    :return: dictionary in the same form as D where every value whose absolute value is less than a threshold is
        replaced with zero
    >>> suppress(forward([1, 2, 3, 4]), 1) == {(2, 0): 0, (1, 0): -2.0, (0, 0): 5.0, (2, 1): 0}
    True
    """
    return {key:(D[key] if abs(D[key]) >= threshold else 0) for key in D.keys()}


# task 10.9.5
def sparsity(D):
    """
    Return percentage of values in D that are non-zero. The smaller the value the better the compression achieved
    :param D: dictionary in the form returned from suppress(D, threshold)
    :return: percentage of keys that are zero
    >>> D = forward([1, 2, 3, 4])
    >>> sparsity(D)
    1.0
    >>> sparsity(suppress(D, 1))
    0.5
    """
    n = len(list(D.keys()))
    return sum([0 if D[key] == 0 else 1 for key in D.keys()]) / n


# task 10.9.6
def unnormalize_coefficients(n, D):
    """
    Functional inverse of normalize_coefficients(n, D)
    :param n: integer dimension of the original space
    :param D: output from normalize_coefficients(n, D)
    :return: equivalent input D to normalize_coefficients(n, D)
    >>> D = forward_no_normalization([1,2,3,4])
    >>> n = len(list(D.keys()))
    >>> Dnorm = normalize_coefficients(n, D)
    >>> D == Dnorm
    False
    >>> Dunnorm = unnormalize_coefficients(n, Dnorm)
    >>> D == Dunnorm
    True
    >>> Dnorm == Dunnorm
    False
    """
    wold = n
    Dc = D.copy()
    while True:
        w = wold // 2
        sq_norm = (n / (4 * w)) ** (1 / 2) if w > 0 else n ** (1 / 2)
        if w == 0:
            Dc[0, 0] = Dc[0, 0] / sq_norm
            break
        Dc.update({(w, i): Dc[(w, i)] / sq_norm for i in range(w)})
        wold = w
    return Dc


"""
left - right = v
left = v + right

    (left + right) / 2 = w
    left + right = 2w
    right = 2w - left

left = v + w2 - left
2left = v + w2
left = v/2 + w

    right = 2w - (v/2 + w)     
"""

# task 10.9.7
def backward_no_normalization(D):
    """
    :param D: dictionary of unnormalized wavelet coefficients
    :return: inverse of of forward_no_normalization(D)
    >>> v1 = [1, 2, 3, 4]
    >>> forward1 = forward_no_normalization(v1)
    >>> backward1 = backward_no_normalization(forward1)
    >>> v1 == backward1
    True
    >>> v2 = [4,5,3,7,4,5,2,3,9,7,3,5,0,0,0,0]
    >>> forward2 = forward_no_normalization(v2)
    >>> backward2 = backward_no_normalization(forward2)
    >>> v2 == backward2
    True
    """
    n = len(D)
    v = [D[(0, 0)]] # the one element list whose entry is the coefficient of B00
    while len(v) < n:
        # k = 2 * len(v)
        # vnew = [ for i in range(k)] # a k element list
        b_ix = len(v)
        vnew = []
        for w_ix, w in enumerate(v):
            v_val = D[(b_ix, w_ix)]
            vnew.append(v_val/2 + w)
            vnew.append(2 * w - (v_val/2 + w))
        v = vnew
    return v


# task 10.9.7
def dictlist_helper(dlist, k):
    from grading.The_Matrix_problems import dictlist_helper as dlh
    return dlh(dlist, k)


# task 10.9.8
def backward(D):
    """
    Computes the inverse wavelet transform. This involves combining unnormalize_coefficients(n, D) and
    backward_no_normalization(D).
    :param D: dictionary as it would come from forward(v)
    :return: inverse of forward(v)
    >>> v = [1, 2, 3, 4]
    >>> D = forward(v)
    >>> backward(D) == v
    True
    """
    return backward_no_normalization(unnormalize_coefficients(len(list(D.keys())), D))


# task 10.9.9
def forward2d(listlist):
    """

    :param listlist: m element list of n element lists with each inner list a row of pixel intensities
        for simplicity assume m and n are powers of 2
    :return: dictdict representation of the wavelet coefficients
    >>> expected = \
    { \
        (2, 1): {(0, 0): -0.7071067811865476}, \
        (2, 0): {(0, 0): -0.7071067811865476}, \
        (1, 0): {(0, 0): -2.0}, \
        (0, 0): {(0, 0): 5.0}, \
    }
    >>> listlist = [[1, 2, 3, 4]]
    >>> forward2d(listlist) == expected
    True
    >>> expected2 = \
    { \
        (2, 1): {(1, 0): -1.0000000000000002, (0, 0): 0.0}, \
        (2, 0): {(1, 0): 0.0, (0, 0): -1.0000000000000002}, \
        (1, 0): {(1, 0): -0.7071067811865476, (0, 0): -2.121320343559643}, \
        (0, 0): {(1, 0): -0.7071067811865476, (0, 0): 7.778174593052023}, \
    }
    >>> listlist2 = [[1, 2, 3, 4], [2, 3, 4, 3]]
    >>> forward2d(listlist2) == expected2
    True
    """
    D_list = [forward(l) for l in listlist]
    L_dict = {key:[D[key] for D in D_list] for key in D_list[0].keys()}
    return {key:forward(L_dict[key]) for key in L_dict.keys()}


# task 10.9.10
def suppress2d(D_dict, threshold):
    """
    Two dimensional of suppress(D, threshold) that suppresses values with absolutes values less than threshold
    in a dictionary of dictionaries such as is returned by forward2d(listlist)
    :param D_dict: dictionary of dictionaries
    :param threshold: value to suppress below
    :return: dictionary of dictionaries with same keys as D_dict
    >>> suppress2d(forward2d([[1, 2, 3, 4]]), 1) == { \
           (2, 0): {(0, 0): 0}, \
           (1, 0): {(0, 0): -2.0}, \
           (0, 0): {(0, 0): 5.0}, \
           (2, 1): {(0, 0): 0} \
        }
    True
    """
    return {key:suppress(D_dict[key], threshold) for key in D_dict.keys()}


# task 10.9.11
def sparsity2d(D_dict):
    """
    two dimensional version of sparsity(D)
    :param D_dict: dictionary of dictionaries
    :return: percentage of keys that are zero
    >>> D_dict = forward2d([[1, 2, 3, 4]])
    >>> sparsity2d(D_dict)
    1.0
    >>> D_dict = forward2d([[1, 2, 3, 4]])
    >>> sparsity2d(suppress2d(D_dict, 1))
    0.5
    """
    return sum([sparsity(D_dict[key]) for key in D_dict.keys()]) / len(list(D_dict.keys()))


# task 10.9.12
def listdict2dict(L_dict, i):
    """
    :param L_dict: dictionary of lists, all same length
    :param i: index in to L_dict lists
    :return: dictionary with same keys as L_dict, in which key k maps to element i of L_dict[i]
    """
    return {key:L_dict[key][i] for key in L_dict.keys()}


# task 10.9.13
def listdict2dictlist(listdict):
    """
    Converts from a listdict representation (a dictionary of lists) to a dictlist representation (a list of dictionaries)
    :param listdict: dictionary of lists
    :return: list of dictionaries
    >>> expected = [\
        {(8, 0): 1, (8, 1): 3}, \
        {(8, 0): 2, (8, 1): 4} \
    ]
    >>> listdict = {(8, 0):[1, 2], (8, 1): [3, 4]}
    >>> listdict2dictlist(listdict) == expected
    True
    """
    n = len(listdict[list(listdict.keys())[0]])
    return [listdict2dict(listdict, i) for i in range(n)]

# def 10.9.14
def backward2d(dictdict):
    """
    Functional inverse of forward2d(listlist)
    :param dictdict: dictionary of dictionaries
    :return: list of lists
    >>> listlist = [[1, 2, 3, 4], [2, 3, 4, 3]]
    >>> dictdict = forward2d(listlist)
    >>> expected = [[0.9999999999999999, 2.0, 3.0, 4.0], [2.0, 3.0, 4.0, 3.0]] # stupid floating point math
    >>> actual = backward2d(dictdict)
    >>> actual == expected
    True
    """
    # Step 1: apply backward(D) to transform each inner dictionar of dictdict to convert to a list results in a listdict
    listdict = {key:backward(dictdict[key]) for key in dictdict.keys()}
    # Step 2: "tranpose"-type step that transforms from a listdict to a dictlist
    dictlist = listdict2dictlist(listdict)
    # Step 3: applies backward(D) to each inner dictionary resulting in a listlist
    return [backward(d) for d in dictlist]


# Task 10.9.16-18
def image_round(image):
    """
    :param image: a grayscale image represented as a list of list of floats
    :return: corresponding image, represented as a list of lists of integers, obtained by rounding the floats in the
        input image and taking their absolute values and replacing numbers greater than 255 with 255
    >>> from resources.image import file2image, color2gray, image2display
    >>> image = color2gray(file2image("../../resources/images/Dali.png"))
    >>> dictdict = forward2d(image)
    >>> # sparsity2d(dictdict) # before suppression it's ~.73
    >>> dictdict_suppressed = suppress2d(dictdict, 1024)
    >>> # sparsity2d(dictdict_suppressed) # ~.35 for threshold of 2
    >>> image2display(image_round(backward2d(dictdict_suppressed)))
    """
    # image2diplay(backward2d(forward2d(image))
    # image2display(image_round(backward2d(forward2d(image))))
    threshold = 255
    return [[int(round(e)) if abs(int(round(e))) < threshold else threshold for e in image[n]] for n in range(len(image))]
