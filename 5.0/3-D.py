n, k = map(int, input().split())
numbers = list(map(int, input().split()))

def hasRepeats(n, k, numbers):
    last_indices = {}
    for i in range(n):
        if last_indices.get(numbers[i]) == None:
            last_indices.update({numbers[i]: i})
        else:
            if i - last_indices.get(numbers[i]) <= k:
                return True
            else:
                last_indices.update({numbers[i]: i})
    return False

result = hasRepeats(n, k, numbers)

print('YES' if result else 'NO')
