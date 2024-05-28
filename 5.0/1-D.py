def canMove(board, x, y):
    if x >= 8 or x < 0 or y >= 8 or y < 0:
        return False
    return board[x][y] == '*' or board[x][y] == '-'

def move(board, x, y):
    if (board[x][y] == '*'):
            board[x][y] = '-'
            return 1
    return 0

def verticalUp(board, x, y):

    count = 0
    x -= 1

    while canMove(board, x, y):
        count += move(board, x, y)
        board[x][y] = '-'
        x -= 1

    return count


def verticalDown(board, x, y):
    count = 0
    x += 1

    while canMove(board, x, y):
        count += move(board, x, y)
        x += 1

    return count

def horizontalLeft(board, x, y):
    count = 0
    y -= 1

    while canMove(board, x, y):
        count += move(board, x, y)
        y -= 1

    return count

def horizontalRight(board, x, y):
    count = 0
    y += 1

    while canMove(board, x, y):
        count += move(board, x, y)
        y += 1

    return count

def diagonalUpLeft(board, x, y):
    count = 0
    x -= 1
    y -= 1

    while canMove(board, x, y):
        count += move(board, x, y)
        x -= 1
        y -= 1

    return count

def diagonalUpRight(board, x, y):
    count = 0
    x -= 1
    y += 1

    while canMove(board, x, y):
        count += move(board, x, y)
        x -= 1
        y += 1

    return count

def diagonalDownLeft(board, x, y):
    count = 0
    x += 1
    y -= 1

    while canMove(board, x, y):
        count += move(board, x, y)
        x += 1
        y -= 1

    return count

def diagonalDownRight(board, x, y):
    count = 0
    x += 1
    y += 1

    while canMove(board, x, y):
        count += move(board, x, y)
        x += 1
        y += 1

    return count

board = []

for i in range(8):
    board.append([char for char in input().strip()])

count = 64

for x in range(8):
    for y in range(8):
        if board[x][y] == 'R':
            count -= 1
            count -= verticalUp(board, x, y)
            count -= verticalDown(board, x, y)
            count -= horizontalLeft(board, x, y)
            count -= horizontalRight(board, x, y)
        elif board[x][y] == 'B':
            count -= 1
            count -= diagonalUpLeft(board, x, y)
            count -= diagonalDownLeft(board, x, y)
            count -= diagonalUpRight(board, x, y)
            count -= diagonalDownRight(board, x, y)

print(count)
