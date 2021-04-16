dp = [0] * 5001
dp[0] = 1
sub = 0

for i in range(2, n + 1, 2):
    dp[i] = (dp[i - 2] * 3  + sub * 2) % 1000000007
    sub += dp[i - 2]

def solution(n):
    return dp[n]