import sys
input = sys.stdin.readline

n = int(input())
dp = [1, 2]

for i in range(n+1):
    dp.append((dp[i] + dp[i+1]) % 15746)

print(dp[n-1])