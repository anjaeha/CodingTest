import sys
input = sys.stdin.readline

n = int(input())
s = [0]
s += list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(n):
    dp[i+1] = dp[i] + s[i+1]

m = int(input())
for case in range(m):
    x, y = map(int, input().split())

    print(dp[y] - dp[x-1])