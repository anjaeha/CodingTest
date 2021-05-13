import sys
input = sys.stdin.readline
from math import factorial

n, k = map(int, input().split())
result = factorial(n) // factorial(n - k) // factorial(k)
print(result % 10007)


"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, k = map(int, input().split())

dp = [[0] * 1 for _ in range(1001)]
dp[1].append(1)

for i in range(2, 1001):
    for j in range(1, i+1):
        if i == 1:
            dp[i].append(1)
        elif i == j:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j])
print(dp[n+1][k+1] % 10007)
"""