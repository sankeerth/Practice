array = [4, 7, 4, 7, 7, 4, 4, 7, 4, 4, 9, 4, 3]


def majority_element_in_array(array):
    """check if an element appears more than half the number of times the size of an array"""
    candidate = None
    count = 0
    n = len(array)

    # initialize count to 0 and set a candidate majority as None
    # set the candidate to current element if count is 0
    # iterate and update the count of the candidate
    # this loop essentially finds the number of times the candidate has appeared consecutively
    # since we need to find the majority element, candidate has to appear consecutively at least once
    # which is the main idea for solving in O(n)
    for i in range(n):
        if count == 0:
            candidate = array[i]
            count = 1
        else:
            if array[i] == candidate:
                count += 1
            else:
                count -= 1

    # if count is 0, then no candidate was found and hence no need to check if it is a majority element
    if count == 0:
        print("No majority candidate found")
        return

    # if count is not 0, then iterate through the array to check if the candidate is a majority element
    # this is needed since a candidate can have a count of more than 0 if it appears consecutively
    # at the end of the array. However, it need not appear more than n/2 times
    count = 0
    for i in range(n):
        if array[i] == candidate:
            count += 1

    if count > n/2:
        print(candidate, "is a majority element")
    else:
        print("No majority candidate found")


majority_element_in_array(array)