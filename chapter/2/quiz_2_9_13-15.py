from chapter2.quiz_2_9_4 import list_dot

haystack_13 = [1, -1, 1, 1, 1, -1, 1, 1, 1]
needle_13 = [1, -1, 1, 1, -1, 1]

haystack_14 = [1,2,3,4,5,6]
needle_14 = [1,2,3]


# note, this does not find the "best" match
# 2.9.15 book answer is wrong, off by 1
def dot_product_list(needle, haystack):
    needle_len = len(needle)
    return [list_dot(needle, haystack[i:needle_len + i])
            for i in range(len(haystack) - needle_len + 1)]


if __name__ == "__main__":
    # [2, 2, 0, 0]
    print(dot_product_list(needle_13, haystack_13))

    # [14, 20, 26, 32]
    print(dot_product_list(needle_14, haystack_14))

