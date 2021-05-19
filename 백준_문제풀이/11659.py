import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [0]
s += list(map(int, input().split()))

dp = [0]
for i in range(1, n+1):
    dp.append(dp[i-1] + s[i])

for i in range(m):
    x, y = map(int, input().split())

    result = dp[y] - dp[x-1]

    print(result)