array = [5, 5, 4, 8, 4, 5, 8, 9, 4, 8]


def number_appears_once_in_array(array, n):
    """find the number that appears once among other numbers that each appear n times in an array"""
    result = [0] * 32

    # store the count of set bits of each number at ith position in an array
    for i in range(len(array)):
        x = array[i]
        j = 0
        while x > 0:
            if x & 0x01 == 1:
                result[j] += 1
            x >>= 1
            j += 1

    # mod the count of set bits at each position with n (times each number appers in the array)
    # result array represents the number that appears once with its bits set to 1 at ith positions
    solution = 0
    for i in range(32):
        result[i] = result[i] % n
        if result[i] == 1:
            solution |= 1 << i
    print(solution)

number_appears_once_in_array(array, 3)