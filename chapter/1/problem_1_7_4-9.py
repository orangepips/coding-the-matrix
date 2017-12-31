# https://github.com/lqxyz/Coding-the-Matrix/blob/master/Week0-The_Function_and_the_Field/The_Field_Problems/The_Field_problems.py#L69

# 'current' should be initialized with the identity element for the <operation>
# i.e. the value 'i' such that i <operation> x == x
# or any value 'x'


def mySum(L):
    current = 0
    for x in L:
        current += x
    return current


def myProduct(L):
    current = 1
    for x in L:
        current *= x
    return current


def myMin(L):
    current = float('infinity')
    for x in L:
        current = x if x < current else current
    return current


def myConcat(L):
    current = ''
    for x in L:
        current += x
    return current


def myUnion(L):
    current = set()
    for x in L:
        current |= x
    return current


if __name__ == "__main__":
    print("mySum")
    print(mySum([1,2,3]))
    print(mySum(set()))

    print("myProduct")
    print(myProduct([1,2,3]))
    print(myProduct(set()))

    print("myMin")
    print(myMin([1,2,3]))
    print(myMin(set()))

    print("myConcat")
    print(myConcat(['A','B','C']))
    print(myConcat([]))

    print("myUnion")
    print(myUnion([{1,2,3}, {2,3,4}, {3,4,5}]))
    print(myUnion([]))

# it's not possible to define the intersection of an empty list of sets because
# see https://en.wikipedia.org/wiki/Intersection_(set_theory)#Nullary_intersection
# see https://math.stackexchange.com/questions/370188/empty-intersection-and-empty-union
