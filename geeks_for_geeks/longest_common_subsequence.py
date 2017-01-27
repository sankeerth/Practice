
str1 = "abc"
str2 = "aed"


def lcs(str1, str2, l1, l2):
    if l1 == 0 or l2 == 0:
        return 0
    elif str1[l1-1] == str2[l2-1]:
        return 1 + lcs(str1, str2, l1-1, l2-1)
    else:
        return max(lcs(str1, str2, l1, l2-1), lcs(str1, str2, l1-1, l2))


print(lcs(str1, str2, len(str1), len(str2)))


"""
Recursive solution with O(2^n)
if last char of both strings are equal :
    L(str1, str2, l1, l2) = 1 + L(str1, str2, l1-1, l2-1)
else
    L(str1, str2, l1, l2) = MAX(L(str1, str2, l1-1, l2), L(str1, str2, l1, l2-1))


str1 = "adx"
str2 = "axg"


def lcs(str1, str2, l1, l2):
    if l1 == 0 or l2 == 0:
        return 0
    elif str1[l1-1] == str2[l2-1]:
        return 1 + lcs(str1, str2, l1-1, l2-1)
    else:
        return max(lcs(str1, str2, l1, l2-1), lcs(str1, str2, l1-1, l2))


print(lcs(str1, str2, len(str1), len(str2)))

"""