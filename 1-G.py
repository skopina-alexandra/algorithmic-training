x = int(input())
y = int(input())
p = int(input())

k = 0

moves = 0
damage = 0

def destroy(x,y,k):
    k -= x - y
    x = x - k

    count = 0

    while x > 0 and k > 0:
        k = k - min(x, k)
        x -= k
        count += 1

    if x <= 0:
        return -1
    else:
        return count

min_moves = -1

while y > 0 and x > 0:
    moves += 1

    if (y <= x):
        moves_to_destroy = destroy(x, y, k)
        if moves_to_destroy >= 0:
            if min_moves < 0:
                min_moves = moves_to_destroy + moves
            else:
                min_moves = min(min_moves, moves + moves_to_destroy)
    if x > k:
        damage = min(y, x - k)
    else:
        damage = 1

    y -= damage

    if k > 0:
        k = k - (x - damage)

    x -= k

    if y > 0:
        k += p

print(min_moves)

