from chapter2.vec import Vec

# included in vecutil.py
def list2vec(L):
    return Vec(set(range(len(L))), {k:v for k,v in enumerate(L)})


if __name__ == "__main__":
    print(list2vec([4,8,9,12]))
