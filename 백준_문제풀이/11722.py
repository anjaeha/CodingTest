import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if s[i] < s[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp)