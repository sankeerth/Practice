class Solution(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = list()
        for i in range(self.rows):
            self.grid.append([0] * self.cols)
        self.num_islands = 0
        self.parent = [i for i in range(rows * cols)]
        self.size = [1] * (rows * cols)

    def display_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.grid[i][j], ' ', end='')
            print()

    def get_root(self, x, y):
        root = self.cols * x + y
        while self.parent[root] != root:
            root = self.parent[root]
        return root

    def find(self, current, adjacent):
        root_x = self.get_root(current)
        root_y = self.get_root(adjacent)
        return root_x == root_y

    def union(self, current, adjacent):
        if self.size[current] < self.size[adjacent]:
            self.parent[current] = adjacent
            self.size[adjacent] += self.size[current]
        else:
            self.parent[adjacent] = current
            self.size[current] += self.size[adjacent]

    def perform_union(self, current, adjacent):
        # islands are already joined
        if current == adjacent:
            return
        self.union(current, adjacent)
        self.num_islands -= 1

    def add_island(self, x, y):
        # island already added
        if self.grid[x][y] == 1:
            return
        else:
            self.grid[x][y] = 1
            self.num_islands += 1

            self.display_grid()
            if x > 0 and self.grid[x-1][y] == 1:
                cur_root = self.get_root(x, y)
                adj_root = self.get_root(x-1, y)
                self.perform_union(cur_root, adj_root)
            if y > 0 and self.grid[x][y-1] == 1:
                cur_root = self.get_root(x, y)
                adj_root = self.get_root(x, y-1)
                self.perform_union(cur_root, adj_root)
            if x < self.rows-1 and self.grid[x+1][y] == 1:
                cur_root = self.get_root(x, y)
                adj_root = self.get_root(x + 1, y)
                self.perform_union(cur_root, adj_root)
            if y < self.cols-1 and self.grid[x][y+1] == 1:
                cur_root = self.get_root(x, y)
                adj_root = self.get_root(x, y+1)
                self.perform_union(cur_root, adj_root)

s = Solution(3, 3)
s.add_island(0,0)
print("'", s.num_islands, "'")
s.add_island(0,1)
print("'", s.num_islands, "'")
s.add_island(1,2)
print("'", s.num_islands, "'")
s.add_island(2,1)
print("'", s.num_islands, "'")
s.add_island(0,2)
print("'", s.num_islands, "'")
s.add_island(2,2)
print("'", s.num_islands, "'")

