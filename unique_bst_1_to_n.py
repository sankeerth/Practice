# array to store the intermediate results as it need not be computed again (DP)
res = [-1] * 6

res[0] = 1
res[1] = 1


def unique_bst_1_to_n(n):
    """finds the unique number of BSTs that can be formed with nodes as values from 1 to n"""
    if res[n] != -1:
        return res[n]

    ans = 0
    for i in range(n):
        ans += unique_bst_1_to_n(i) * unique_bst_1_to_n(n-i-1)

    res[n] = ans
    return ans

print(unique_bst_1_to_n(5))