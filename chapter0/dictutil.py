# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[key] for key in keylist]

def list2dict(L, keylist): return {k:v for (k,v) in zip(keylist,L)}

def listrange2dict(L): return list2dict(L, range(len(L)))

def makeInverseIndex(strlist):
    inverseIndex = dict()
    for ix, doc in enumerate(strlist):
        for word in doc.split():
            word = word.lower()
            if word in inverseIndex:
                inverseIndex[word].add(ix)
            else:
                inverseIndex[word] = {ix}
    return inverseIndex

def orSearch(inverseIndex, query):
    matches = set()
    for word in query:
        word = word.lower()
        if word in inverseIndex:
            matches |= inverseIndex[word]
    return matches

def andSearch(inverseIndex, query):
    matches = None
    for word in query:
        word = word.lower()
        if word in inverseIndex:
            if matches is None:
                matches = inverseIndex[word]
            else:
                matches &= inverseIndex[word]
        else:
            return {}
    return matches

def increments(L): return [n+1 for n in L]

def cubes(L): return [n**3 for n in L]

def tuple_sum(A, B): return [(x[0] + y[0], x[1] + y[1]) for (x, y) in zip(A, B)]

def inv_dict(d): return {d[k]:k for k in d.keys()}

def row(p, n): return [p+ix for ix in range(n)]

'''
twenty_element_list = list(range(20))
fifteen_element_list_twenty_elements_each = [twenty_element_list] * 15

[dictutil.row(p, 20) for p in range(15)]

[[p+ix for ix in range(20)] for p in range(15)]


1 1 .2
2 2 .2
3 0 .2
4 1 .1
5 2 .1
6 0 .1
7 1 .1

1 = .2 + .1 + .1 = .4
0 or 2 = .2 + .2 + .1 + .1 = .6
'''
