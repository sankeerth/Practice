array = [73, 85, 94, 21, 27, 34, 47, 54, 66]
array = [5, 5, 5, 0, 1, 2, 5]
array = [1, 1, 1, 1, 1]

def pivot_in_sorted_rotated_array(array):
    """find the least element in the array which is the start of the sorted array"""

    n = len(array)

    # array is empty
    if n == 0:
        return None

    # only 1 element in the array
    if n == 1:
        return 0

    # array is not rotated and hence it is already in order
    if array[0] < array[n-1]:
        return 0

    # if all elements in array are same
    if array[0] == array[n-1] and array[0] == array[1]:
        return 0

    low = 0
    high = n - 1

    while low <= high:
        mid = int(low + (high - low)/2)

        # return mid if it is the pivot
        if array[mid] > array[mid+1]:
            return mid + 1
        elif array[mid-1] > array[mid]:
            return mid

        if array[low] < array[mid]:
            low = mid + 1
        else:
            high = mid - 1


print(pivot_in_sorted_rotated_array(array))