dp = [0 for _ in range(2001)]
dp[1] = 1
dp[2] = 2
for i in range(3, 2001):
    dp[i] = (dp[i-1] + dp[i-2]) % 1234567

def solution(n):
    return dp[n]