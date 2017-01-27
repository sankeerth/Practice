class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        res = list()
        x = int(area ** 0.5)
        while not area % x == 0:
            x -= 1
        y = int(area/x)
        print(y, x)


s = Solution()
s.constructRectangle(990)

