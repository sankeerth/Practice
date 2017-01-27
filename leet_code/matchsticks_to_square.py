from collections import OrderedDict, defaultdict

array = [3,1,1,2,2,2,1,3,4,5]
array = [5,5,5,5,4,4,4,4,3,3,3,3]


def matchsticks_to_square(array):
    """Return True if a square can by built by using all the matchsticks"""

    num_sticks = len(array)
    sticks_sum = sum(array)
    len_of_square = int(sticks_sum/4)

    data = defaultdict(int)
    for x in array:
        data[x] += 1
    sticks = sorted(data.keys(), reverse=True)

    distinct_sticks = len(sticks)

    # corner cases:
    # 1. if number of sticks less than 4
    # 2. if the sum of all matchsticks is not divisible by 4. So square not possible
    # 3. if the longest stick is greater than the length of square then that stick cannot
    # be used to build the square
    if num_sticks < 4:
        return False
    elif sticks_sum % 4 != 0:
        return False
    elif len_of_square < sticks[0]:
        return False

    i = 0
    while i < distinct_sticks:
        while data[sticks[i]]:
            if build_square(data, sticks, i, distinct_sticks, len_of_square):
                pass
            else:
                return False
        i += 1
    return True


def build_square(data, sticks, i, n, remaining_len):
    """Backtracking solution
    scan from the longest stick and check if a side can be
    constructed with the help of other sticks. key is to traverse
    the sticks from longest to shortest, otherwise, a side can
    accidentally be formed by shorter sticks (eg: 1,1,1,1..) and
    longer sticks cannot use this short sticks to form a side since they
    would be exhausted"""

    for j in range(i, n):
        if data[sticks[j]] and remaining_len >= sticks[j]:
            data[sticks[j]] -= 1
            remaining_len -= sticks[j]
            if remaining_len == 0:
                return True
            if build_square(data, sticks, i, n, remaining_len):
                return True
            else:
                data[sticks[j]] += 1
                remaining_len += sticks[j]
    return False


print(matchsticks_to_square(array))

"""
    while i < distinct_sticks:
        while not data[sticks[i]]:
            remaining_len = len_of_square
            remaining_len -= data[sticks[i]]
            data[sticks[i]] -= 1
            k = i
            for j in range(k, distinct_sticks):
                if data[sticks[j]] and data[sticks[j]] >= remaining_len:
                    remaining_len -= data[sticks]

"""