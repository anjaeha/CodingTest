n = int(input())

day = []
pay = []

for _ in range(n):
    x, y = map(int, input().split())
    day.append(x)
    pay.append(y)

dp = [0] * (n + 1)
for i in range(n -1, -1, -1):
    if i + day[i] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + day[i]] + pay[i])

print(dp[0])