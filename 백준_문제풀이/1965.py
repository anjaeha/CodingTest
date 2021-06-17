import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    for j in range(n):
        if s[i] > s[j] and dp[i] < dp[j]:
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))