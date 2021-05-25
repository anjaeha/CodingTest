import sys
input = sys.stdin.readline

n = int(input())
hp = list(map(int, input().split()))
p = list(map(int, input().split()))

dp = [[0] * 101 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if j >= hp[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hp[i-1]] + p[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])