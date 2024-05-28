n = int(input())
ropes = list(map(int, input().split()))

sum = 0
max_len = 0

for rope in ropes:
    max_len = max(max_len, rope)
    sum += rope

result = 2 * max_len - sum if max_len > sum - max_len else sum

print(result)