n, k = map(int, input().split())
numbers = list(map(int, input().split()))

def hasRepeats(n, k, numbers):
    current_window = set(numbers[1 : k + 1])
    count = len(numbers)
    for i in range(count - 1):
        if numbers[i] in current_window:
            return True
        current_window.discard(numbers[i + 1])
        if i + k < count:
            current_window.add(numbers[i + k])
    return False

result = hasRepeats(n, k, numbers)

print('YES' if result else 'NO')
