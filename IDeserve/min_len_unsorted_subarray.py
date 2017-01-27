array = [1, 4, 7, 3, 10, 48, 17, 26, 30, 45, 50, 62]


def min_len_unsorted_subarray(array):
    """Minimum length subarray of an unsorted array
    sorting which results in complete sorted array"""

    n = len(array)
    start_index = 0
    end_index = n-1

    # traverse from start to find the start_index where array[i] > array[i+1]
    while start_index < n-1 and array[start_index] < array[start_index+1]:
        start_index += 1

    # traverse from end to find the end_index where array[n-i-1] > array[n-i]
    while end_index > 0 and array[end_index] > array[end_index-1]:
        end_index -= 1

    # array is already sorted
    if start_index > end_index:
        return 0, 0

    min_element = float('inf')
    max_element = float('-inf')

    # find the min and max elements between start_index and end_index
    for i in range(start_index, end_index+1):
        if array[i] < min_element:
            min_element = array[i]
        if array[i] > max_element:
            max_element = array[i]

    min_index = 0
    max_index = n-1

    # search sorted array from start to start_index to find index at which
    # min_element will be sorted array
    while min_index < start_index and array[min_index] < min_element:
        min_index += 1

    # search sorted array from end_index to end to find index at which
    # max_element will be sorted array
    while max_index > end_index and array[max_index] > max_element:
        max_index -= 1

    # return the indices between which the array has to be sorted
    return min_index, max_index

print(min_len_unsorted_subarray(array))
