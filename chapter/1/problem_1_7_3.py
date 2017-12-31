def my_function_composition(f, g): return {k:g[f[k]] for k in f.keys()}

if __name__ == "__main__":
    f = {0:'a', 1:'b'}
    g = {'a':'apple', 'b':'banana'}
    print(my_function_composition(f, g))