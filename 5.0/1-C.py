n = int(input())

result = 0
remainder = 0

for i in range(n):
    a = int(input())
    result += a // 4
    remainder = a % 4;
    if remainder == 1:
        result += 1
    elif remainder == 2 or remainder == 3:
        result += 2

print(result)
