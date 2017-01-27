def radix_sort(nums):
    radix = 11
    max_element = max(nums)
    exp = 1
    N = len(nums)
    aux = [0 for i in range(N)]

    while max_element > 0:
        print(max_element)
        count = [0 for i in range(radix)]

        # counting sort
        for i in range(N):
            count[(int(nums[i]/exp) % 10)+1] += 1

        # cumulation
        for i in range(1, radix):
            count[i] += count[i-1]
        print(count)

        # sort the numbers with respect to the current digit place
        for i in range(N):
            aux[count[int(nums[i]/exp) % 10]] = nums[i]
            count[int(nums[i] / exp) % 10] += 1
        print(aux)

        # copy aux array to nums array
        for i in range(N):
            nums[i] = aux[i]

        # reduce the max element and multiply the divisor by 10 to get the next significant bit
        max_element = int(max_element/10)
        exp *= 10


nums = [274, 209, 34, 9, 21]
radix_sort(nums)
