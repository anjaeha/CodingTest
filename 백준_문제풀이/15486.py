import sys
input = sys.stdin.readline

n = int(input())
p = []
t = []
dp = []

for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
    dp.append(y)

dp.append(0)

for i in range(n-1, -1, -1):
    if i + t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i + t[i]])

print(dp[0])