import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = []

for i in range(n):
    s.append(int(input()))
s.sort()

dp = [999999] * (k+1)
dp[0] = 0

for i in s:
    for j in range(i, k+1):
        dp[j] = min(dp[j - i] + 1, dp[j])

print(dp[-1] if dp[-1] != 999999 else - 1)