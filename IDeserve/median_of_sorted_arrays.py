a = [1, 3, 5, 11, 17]
b = [9, 10, 11, 13, 14]

#a = [1, 3]
#b = [2]

def median_of_sorted_arrays(a, b, start_a, end_a, start_b, end_b):
    mid_a = int(start_a + (end_a - start_a)/2)
    mid_b = int(start_b + (end_b - start_b)/2)

    median_a = a[mid_a]
    median_b = b[mid_b]

    """
    # TODO : for arrays of different lengths, currently returns error
    if start_a == end_a or start_b == end_b:
        if start_a == end_a and start_b == end_b:
            return (a[start_a] + b [start_b])/2
        else:
            return median_a if median_a > median_b else median_b
    """

    if end_a - start_a == 1 and end_b - start_b == 1:
        return (max(a[start_a], b[start_b]) + min(a[end_a], b[end_b]))/2

    if median_a == median_b:
        return median_a
    elif median_a < median_b:
        start_a = mid_a
        end_b = mid_b
    else:
        end_a = mid_a
        start_b = mid_b

    return median_of_sorted_arrays(a, b, start_a, end_a, start_b, end_b)


print(median_of_sorted_arrays(a, b, 0, len(a)-1, 0, len(b)-1))