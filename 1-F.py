n = int(input())
a = list(map(int,input().split()))
res_odd = a[0] % 2 == 1
plus = chr(43)
mult = chr(120)
ans = ''

for i in range(1, n):
    if res_odd and a[i] % 2 == 1:
        ans += mult
    else:
        ans += plus
        if not res_odd:
            res_odd = a[i] % 2 == 1
print(ans)