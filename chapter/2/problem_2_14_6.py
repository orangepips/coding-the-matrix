from itertools import product

from resources.vecutil import list2vec

from resources.GF2 import one

a = list2vec([one, one, 0, 0])
b = list2vec([one, 0, one, 0])
c = list2vec([one, one, one, one])

x = None

for combo in product([0, one], repeat=4):
    x = list2vec(combo)
    if x * a == one and x * b == one and x * c == one: break

print(repr(x))

y = x + list2vec([one, one, one, one])
print(repr(y))
print(y * b == one and y * b == one and y * c == one)
