# Not solved - Contest 16B

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        x = int(n)
        y = int(int(n) ** 0.5) + 1

        for i in range(2, y):
            while True:
                if x == 1:
                    return str(i)
                if x % i == 1:
                    x = int(x/i)
                else:
                    break
            x = int(n)
        return str(int(n)-1)

s = Solution()
print(s.smallestGoodBase("14919921443713776"))
