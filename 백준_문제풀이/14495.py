n = int(input())
dp = [1 for _ in range(117)]

for i in range(3, 117):
    dp[i] = dp[i-1] + dp[i-3]

print(dp[n - 1])