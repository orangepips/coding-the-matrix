from vecutil import list2vec

e0 = list2vec([1,0])
e1 = list2vec([0,1])

a0 = list2vec([1,2])
a1 = list2vec([3,4])
a2 = list2vec([1,1]) # added to solve

print(e0 == a1 - 2 * a0)
print(e1 == a0 - a2)

b0 = list2vec([1,1])
b1 = list2vec([2,2])
b2 = list2vec([3,3])
b3 = list2vec([0,1]) # added to solve

print(e0 == b0 - b3)
print(e1 == b3)

c0 = list2vec([1,1])
c1 = list2vec([1, -1])
c2 = list2vec([0,1])

print(e0 == c0 - c2)
print(e1 == c2)