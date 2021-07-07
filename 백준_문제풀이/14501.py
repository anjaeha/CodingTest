import sys
input = sys.stdin.readline

n = int(input())
day = []
money = []
dp = []

for i in range(n):
    x, y = map(int, input().split())
    day.append(x)
    money.append(y)
    dp.append(y)
dp.append(0)

for i in range(n-1, -1, -1):
    if i + day[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], money[i] + dp[i + day[i]])

print(dp[0])
