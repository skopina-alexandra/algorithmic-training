n, k, d = map(int,input().split())

result = n * 10
remainder = result % k

if remainder > 0:
    add = k - remainder
    if add < 10:
        result += add
    else:
        result = -1;

if result > 0 and d > 1:
    print(str(result) + '0' * (d - 1))
else:
    print(result)
