import sys
input = sys.stdin.readline

n, k = map(int, input().split())

w = []
v = []

for i in range(n):
    x, y = map(int, input().split())
    w.append(x)
    v.append(y)

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= w[i-1]:
            dp[i][j] = max(dp[i-1][j], v[i-1] + dp[i-1][j-w[i-1]])
        else:
            dp[i][j] = dp[i-1][j]


print(dp[n][k])