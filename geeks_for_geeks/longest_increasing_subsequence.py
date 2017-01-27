data = [10, 22, 9, 33, 21, 50, 41, 60, 80]


def binary_search(increasing_sub, current, index_in_sub):
    low = 0
    high = index_in_sub
    while low <= high:
        mid = low + (high - low)//2
        if current < increasing_sub[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low

def longest_increasing_subsequence(X):
    # initializing variables
    parent = [0 for x in range(len(data))]
    increasing_sub = [0 for x in range(len(data)+1)]
    index_in_sub = 0
    increasing_sub[0] = data[0]
    parent[0] = -1

    for i in range(1, len(data)):
        # append current if greater than last in increasing subsequence array
        if data[i] > increasing_sub[index_in_sub]:
            index_in_sub += 1
            increasing_sub[index_in_sub] = data[i]
        # replace the element greater than current with current
        else:
            index_to_replace = binary_search(increasing_sub, data[i], index_in_sub)
            increasing_sub[index_to_replace] = data[i]

        parent[i] = increasing_sub[index_in_sub-1]

print(longest_increasing_subsequence(data))




"""
Working code of LIS O(n2)

def lis(data):
    indices = [1 for x in range(len(data))]
    lists = []
    for i in range(len(data)):
        l = []
        for j in range(i):
            if data[i] > data[j]:
                if indices[i] < indices[j] + 1:
                    l.append(data[j])
                    indices[i] = indices[j] + 1
        l.append(data[i])
        lists.append(l)
    return lists[indices.index(max(indices))]


print(lis(data))
"""

"""
Written iteratively but there is a bug if the input is: [100, 22, 9, 33, 21, 50, 41, 60, 80]

d = dict()

def lis():
    for i in range(len(data)):
        val = data[i]
        l = []
        l.append(val)
        for j in range(i+1, len(data)):
            next_val = data[j]
            if next_val > val:
                l.append(next_val)
            val = next_val

        d[i] = l

lis()
print(d.values())

max_items = 0
max_index = 0

for k in d.keys():
    num_items = len(d[k])
    if num_items > max_items:
        max_items = num_items
        max_index = k


print("LIS: ", d[max_index])

"""