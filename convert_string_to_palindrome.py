# This question was created by me confusing with the shortest palindrome question in leetcode
# whic c

def convert_string_to_palindrome(s):
    """Convert the given string to shortest palindrome by appending
    characters anywhere in the string"""

    res = list()
    i, j = 0, len(s) - 1
    # print i, j

    while i != j and i < j:
        print
        i, j
        if s[i] == s[j]:
            res.append(s[i])
            i += 1
            j -= 1
        else:
            res.append(s[j])
            j -= 1
        print
        res

    while i < len(s):
        res.append(s[i])
        i += 1

    return ''.join(res)


print(convert_string_to_palindrome("aacecdaa"))