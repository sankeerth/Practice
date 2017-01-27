class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)

        if l % 2 == 0:
            return True
        else:
            s = sum(nums)
            odd, even = 0, 0

            if nums[0] > nums[l-1]:
                for i in range(1, l, 2):
                    odd += nums[i]
                even = s - odd - nums[0]

                if odd > even + nums[0] or even > odd + nums[0]:
                    return False
                else:
                    return True
            else:
                for i in range(0, l-1, 2):
                    odd += nums[i]
                even = s - odd - nums[l-1]

                if odd > even + nums[l-1] or even > odd + nums[l-1]:
                    return False
                else:
                    return True


s = Solution()
print(s.PredictTheWinner([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
