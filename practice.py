class Solution(object):
    def __init__(self, matrix):
        self.res = 0
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.longest_path_matrix = list()
        for i in range(self.rows):
            self.longest_path_matrix.append([0] * self.cols)

    def longest_path(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print('i:', i, 'j:', j)
                self.res = max(self.res, self.longest_path_util(i, j))
                self.display_grid()

    def display_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.longest_path_matrix[i][j], end=' ')
            print()

    def longest_path_util(self, i, j):
        if self.longest_path_matrix[i][j] != 0:
            return self.longest_path_matrix[i][j]

        # store the current value of the matrix
        cur = self.matrix[i][j]
        # put some character to indicate that this was visited
        self.matrix[i][j] = 'O'

        up, left, down, right = 0, 0, 0, 0

        if i > 0 and self.matrix[i-1][j] != 'O' and cur < self.matrix[i-1][j]:
            up = self.longest_path_util(i-1, j)
        if j > 0 and self.matrix[i][j-1] != 'O' and cur < self.matrix[i][j-1]:
            left = self.longest_path_util(i, j-1)
        if i < self.rows - 1 and self.matrix[i+1][j] != 'O' and cur < self.matrix[i+1][j]:
            down = self.longest_path_util(i+1, j)
        if j < self.cols - 1 and self.matrix[i][j+1] != 'O' and cur < self.matrix[i][j+1]:
            right = self.longest_path_util(i, j+1)

        longest_path = max(max(up, left), max(down, right)) + 1
        self.longest_path_matrix[i][j] = longest_path
        self.matrix[i][j] = cur
        return longest_path


matrix = [[18,17,14,11,10,15,14],[16,18,0,17,17,18,12],[2,18,18,7,7,15,17],[18,7,10,6,14,2,14],[16,18,11,15,12,0,9],[17,15,13,13,19,17,16],[0,9,10,0,5,1,7]]
s = Solution(matrix)
s.longest_path()
print('longest path:', s.res)
