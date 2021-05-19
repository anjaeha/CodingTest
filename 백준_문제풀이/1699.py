import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 100001

for i in range(1, n+1):
    dp[i] = i
    for j in range(1, i):
        if i < j * j:
            break

        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1

print(dp[n])