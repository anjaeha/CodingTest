import sys
sys.setrecursionlimit(10000)

dp = [0] * 100001
dp[1] = 1

def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    for i in range(2, len(dp)):
        dp[i] = (dp[i-1] + dp[i-2] ) % 1234567

    return dp[n]


# print(solution(5))