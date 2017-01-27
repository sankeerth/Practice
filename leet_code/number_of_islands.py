data = ["11110","11010","11000","00000"]
data = ["111","010","111"]

grid = list()

for d in data:
    grid.append(list(d))


def display_island():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], ' ', end='')
        print("")


def number_of_islands(grid):
    row = len(grid)
    col = len(grid[0])
    group = 1

    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                group += 1
                dfs(grid, i, j, row, col, group)

    return group - 1


def dfs(grid, i, j, row, col, group):
    grid[i][j] = group

    # Check up
    if i >= 1 and grid[i-1][j] == '1':
        dfs(grid, i-1, j, row, col, group)
    # Check left
    if j >= 1 and grid[i][j-1] == '1':
        dfs(grid, i, j-1, row, col, group)
    # Check down
    if i+1 < row and grid[i+1][j] == '1':
        dfs(grid, i+1, j, row, col, group)
    # Check right
    if j+1 < col and grid[i][j+1] == '1':
        dfs(grid, i, j+1, row, col, group)

display_island()
print(" ")
print(number_of_islands(grid))
print("")
display_island()