import sys
input = sys.stdin.readline

n, k = map(int, input().split())

imp, time = [], []

for i in range(k):
    x, y = map(int, input().split())
    imp.append(x)
    time.append(y)

dp = [[0] * (n+1) for _ in range(k+1)]

for i in range(1, k+1):
    for j in range(1, n+1):
        if j >= time[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i-1]] + imp[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[k][n])