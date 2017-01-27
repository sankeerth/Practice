class Solution(object):
    def __init__(self):
        self.maxlen = 0

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix:
            row = len(matrix)
            col = len(matrix[0])
            for i in range(row):
                for j in range(col):
                    self.findPath(matrix, i, j, row - 1, col - 1, 0)
        return self.maxlen

    def findPath(self, matrix, i, j, row, col, length):
        cur = matrix[i][j]
        matrix[i][j] = 'O'
        length += 1
        if length > self.maxlen:
            self.maxlen = length
        # print matrix, length
        if i > 0 and matrix[i - 1][j] != 'O' and matrix[i - 1][j] > cur:
            self.findPath(matrix, i - 1, j, row, col, length)
        if j > 0 and matrix[i][j - 1] != 'O' and matrix[i][j - 1] > cur:
            self.findPath(matrix, i, j - 1, row, col, length)
        if i < row and matrix[i + 1][j] != 'O' and matrix[i + 1][j] > cur:
            self.findPath(matrix, i + 1, j, row, col, length)
        if j < col and matrix[i][j + 1] != 'O' and matrix[i][j + 1] > cur:
            self.findPath(matrix, i, j + 1, row, col, length)

        length -= 1
        matrix[i][j] = cur

s = Solution()
print(s.longestIncreasingPath([[18,17,14,11,10,15,14],[16,18,0,17,17,18,12],[2,18,18,7,7,15,17],[18,7,10,6,14,2,14],[16,18,11,15,12,0,9],[17,15,13,13,19,17,16],[0,9,10,0,5,1,7]]))