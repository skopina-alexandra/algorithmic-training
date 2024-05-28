k = int(input())

x,y = map(int, input().split())

min_x = x
max_x = x
min_y = y
max_y = y

for i in range(1, k):
    x,y = map(int, input().split())
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

# if max_x == min_x:
    # min_x -= 1

# if max_y == min_y:
    # min_y -= 1

print(min_x, min_y, max_x, max_y)