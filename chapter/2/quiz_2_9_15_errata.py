# submitted to info@codingthematrix.com

# 2.9.4 quiz
def list_dot(u, v):
    return sum([a * b for (a, b) in zip(u, v)])

# 2.9.15 quiz book answer
def dot_product_list(needle, haystack):
    s = len(needle)
    return [list_dot(needle, haystack[i:i+s])
            for i in range(len(haystack) - s)]

# 2.9.15 corrected to address off-by-one error ("s + 1")
def dot_product_list_corrected(needle, haystack):
    s = len(needle)
    return [list_dot(needle, haystack[i:i+s])
            for i in range(len(haystack) - s + 1)]

"""
Calculates the result based on the "is_original" boolean 

Output: 
{quiz} [Original|Corrected] {answer} == {result}: {result == answer} 
"""
def print_result(is_original, quiz, needle, haystack, answer):
    result = dot_product_list(needle, haystack) if is_original \
        else dot_product_list_corrected(needle, haystack)
    print(("{0} " + ("Original" if is_original else "Corrected") + " {1} == {2}: {3}")
          .format(quiz, answer, result, result == answer))


if __name__ == "__main__":
    haystack_2_9_13 = [1, -1, 1, 1, 1, -1, 1, 1, 1]
    needle_2_9_13 = [1, -1, 1, 1, -1, 1]
    answer_2_9_13 = [2, 2, 0, 0]
    print_result(True, "2.9.13", needle_2_9_13, haystack_2_9_13, answer_2_9_13)
    print_result(False, "2.9.13", needle_2_9_13, haystack_2_9_13, answer_2_9_13)

    haystack_2_9_14 = [1, 2, 3, 4, 5, 6]
    needle_2_9_14 = [1, 2, 3]
    answer_2_9_14 = [14, 20, 26, 32]
    print_result(True, "2.9.14", needle_2_9_14, haystack_2_9_14, answer_2_9_14)
    print_result(False, "2.9.14", needle_2_9_14, haystack_2_9_14, answer_2_9_14)


