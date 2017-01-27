from collections import deque

array = [2, 3, 1, 1, -1, 6, 4, 3, 8]


def min_len_subarray_sum_k(array, k):
    if not array:
        return None
    dq = deque()
    current_sum = 0
    start = -1
    end = -1
    min_length = float('inf')

    for i in range(len(array)):
        if current_sum == k:
            if (dq[-1] - dq[0]) + 1 < min_length:
                start = dq[0]
                end = dq[-1]
                min_length = (dq[-1] - dq[0]) + 1
        while dq and (current_sum + array[i]) > k:
            current_sum -= array[dq[0]]
            dq.popleft()
        dq.append(i)
        current_sum += array[i]

    # to take care of the last index as the loop exits before checking this condition
    if current_sum == k:
        if (dq[-1] - dq[0]) + 1 < min_length:
            start = dq[0]
            end = dq[-1]
            min_length = (dq[-1] - dq[0]) + 1

    return start, end


print(min_len_subarray_sum_k(array, 7))