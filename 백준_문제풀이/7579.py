n, k = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
sumCost = sum(cost) + 1

dp = [-1] * sumCost
dp[0] = 0

for i in range(n):
    for j in range(sumCost - 1, -1, -1):
        if dp[j] != -1:
            dp[j + cost[i]] = max(dp[j + cost[i]], dp[j] + memory[i])

for i in range(sumCost):
    if dp[i] >= k:
        print(i)
        break