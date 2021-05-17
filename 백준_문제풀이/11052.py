import sys
input = sys.stdin.readline

n = int(input())

s = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

dp[1] = s[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + s[j]:
            dp[i] = dp[i-j] + s[j]

print(max(dp))