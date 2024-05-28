n, k = map(int, input().split())
prices = list(map(int, input().split()))

profit = 0

if n > 1:
    for i in range(n - k):
        buy = prices[i]
        sell = max(prices[i + 1 : i + k + 1])
        profit = max(profit, sell - buy)

    if k > 1:
        segment = k
        while k > 1:
            k -= 1
            buy = prices[n - 1 - k]
            sell = max(prices[n - k : n])
            profit = max(profit, sell - buy)

print(profit)