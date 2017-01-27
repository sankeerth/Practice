data = ["XXXXXX", "XOOXXX", "XXOOXX", "XOXOXO", "XOXOXO", "XXXOXX"]
#data = ["XOXOXO","OXOXOX","XOXOXO","OXOXOX"]
board = list()

for d in data:
    board.append(list(d))


def display_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], ' ', end='')
        print("")


def solve_dfs(board):
    """Worked in leetcode"""
    row = len(board)
    col = len(board[0])

    for i in range(col):
        dfs(board, 0, i, row, col)
        if row > 1:
            dfs(board, row-1, i, row, col)

    for i in range(row):
        dfs(board, i, 0, row, col)
        if col > 1:
            dfs(board, i, col - 1, row, col)

    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O':
                board[i][j] = 'X'

    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                board[i][j] = 'O'


def solve_bfs(board):
    """Time limit exceeds in leetcode. Don't know what could be the reason"""
    row = len(board)
    col = len(board[0])

    for i in range(col):
        bfs(board, 0, i, row, col)
        if row > 1:
            bfs(board, row - 1, i, row, col)

    for i in range(row):
        bfs(board, i, 0, row, col)
        if col > 1:
            bfs(board, i, col - 1, row, col)

    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O':
                board[i][j] = 'X'

    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                board[i][j] = 'O'


def bfs(board, i, j, row, col):
    if board[i][j] == 'O':
        q = list()
        q.append((i, j))
        while q:
            cur_i, cur_j = q.pop(0)
            board[cur_i][cur_j] = 1

            if cur_i > 1 and board[cur_i-1][cur_j] == 'O':
                q.append((cur_i-1, cur_j))
            if cur_j > 1 and board[cur_i][cur_j-1] == 'O':
                q.append((cur_i, cur_j-1))
            if cur_i+1 < row and board[cur_i+1][cur_j] == 'O':
                q.append((cur_i+1, cur_j))
            if cur_j+1 < col and board[cur_i][cur_j+1] == 'O':
                q.append((cur_i, cur_j+1))


def dfs(board, i, j, row, col):
    if board[i][j] == 'O':
        board[i][j] = 1

        if i > 1:
            dfs(board, i-1, j, row, col)
        if j > 1:
            dfs(board, i, j-1, row, col)
        if i+1 < row:
            dfs(board, i+1, j, row, col)
        if j+1 < col:
            dfs(board, i, j+1, row, col)


display_board()
print("------")
solve_bfs(board)
display_board()