from resources.vecutil import list2vec

x = list2vec([3, 0, 0])
y = list2vec([0, 2, 0])
z = list2vec([0, 0, 1])

a1 = list2vec([2, 0, 1])
a2 = list2vec([1, 0, 2])
a3 = list2vec([2, 2, 2])
a4 = list2vec([0, 1 ,0])

print(x == 3 * a3 - 6 * a4 - 3 * a2)
print(y == 2 * a4)
print(z == - 2 * a4 + a3 - a1)