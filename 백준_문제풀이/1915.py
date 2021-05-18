import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = []
for i in range(n):
    s.append(list(map(int, input().strip())))

dp = [[0] * (m+1) for _ in range(n+1)]

MAX = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if s[i-1][j-1] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

            if dp[i][j] > MAX:
                MAX = dp[i][j]

print(MAX ** 2)