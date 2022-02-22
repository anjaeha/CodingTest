n, k = map(int, input().split())

w = [0]
v = [0]

for _ in range(n):
    x, y = map(int, input().split())
    w.append(x)
    v.append(y)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= w[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])