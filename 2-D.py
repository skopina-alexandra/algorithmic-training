board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

n = int(input())

coordinates = []

for i in range (n):
    x, y = map(int, input().split())
    board[x][y] = 0
    coordinates.append([x, y])

dx = [-1, 1]
dy = [-1, 1]

p = 0

for coord in coordinates:
    for x in dx:
        p += board[coord[0] + x][coord[1]]
    for y in dy:
        p += board[coord[0]][coord[1] + y]

print(p)