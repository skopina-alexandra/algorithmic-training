def search(l, r, numbers, n):
    left, m = 0, 0
    right = n - 1

    while left != right:
        m = (right + left) // 2
        if numbers[m] >= l:
            right = m
        else:
            left = m + 1

    if numbers[left] < l:
        left += 1

    left_answer = left
    left = m
    right = n - 1

    while left != right:
        m = (right  + left) // 2
        if numbers[m] <= r:
            left = m + 1
        else:
            right = m

    if numbers[right] > r:
        right -= 1

    return right - left_answer + 1


n = int(input())
numbers = sorted(list(map(int, input().split())))
k = int(input())

result = []

for i in range(k):
    l, r = map(int, input().split())
    result.append(search(l, r, numbers, n))

print(' '.join(map(str, result)))