import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

dp = [0] * n
dp[0] = s[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + s[i], s[i])

print(max(dp))