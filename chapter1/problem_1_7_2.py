def my_lists(L): return [list(range(1,x)) for x in L]

if __name__ == "__main__":
    print(my_lists([1,2,4]))
    print(my_lists([0]))