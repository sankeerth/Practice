array = [1,3,-1,-3,5,3,6,7]
array = [3, 1, 5, 5, 4, 3]
#array = [2,1,3,4,6,3,8,9,10,12,56]
array = [4, 3, 7, 1]


def sliding_window_maximum(array, k):
    n = len(array)
    max_from_left = [0] * n
    max_from_right = [0] * n
    sliding_max = [0] * (n-k+1)

    max_from_left[0] = array[0]
    max_from_right[n-1] = array[n-1]

    i = 1
    j = n - 2

    while i < n:
        # store the max element encountered when traversed from left
        # reset max element to element in array after each window
        # this has all past max elements
        if i % k == 0:
            max_from_left[i] = array[i]
        else:
            if array[i] > max_from_left[i-1]:
                max_from_left[i] = array[i]
            else:
                max_from_left[i] = max_from_left[i-1]

        # store the max element encountered when traversed from right
        # reset max element to element in array after each window
        # this has all future max elements
        if (j+1) % k == 0:
            max_from_right[j] = array[j]
        else:
            if array[j] > max_from_right[j+1]:
                max_from_right[j] = array[j]
            else:
                max_from_right[j] = max_from_right[j+1]

        i += 1
        j -= 1

    # compare the max of ith element in max_from_right to i+k-1th element in max_from_left
    # and assign it to the sliding_max for that particular sliding window
    for i in range(len(sliding_max)):
        sliding_max[i] = max(max_from_right[i], max_from_left[i+k-1])

    print(max_from_left)
    print(max_from_right)
    print(sliding_max)


from collections import deque

# solution from leetcode user
class Solution(object):
    def maxSlidingWindow(nums, k):
        if not nums: return []
        res = []
        dq = deque()  # store index
        for i in range(len(nums)):
            if dq and dq[0]<i-k+1:  # out of the window
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:  # remove impossible candidate
                dq.pop()
            dq.append(i)
            if i>k-2:
                res.append(nums[dq[0]])
        return res

sliding_window_maximum(array, 2)

print(Solution.maxSlidingWindow(array, 2))