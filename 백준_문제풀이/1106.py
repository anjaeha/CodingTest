import sys
input = sys.stdin.readline

c, n = map(int, input().split())

dp = [100001] * (c+101)
dp[0] = 0

for _ in range(n):
    cost, man = map(int, input().split())
    for i in range(man, 101+c):
        dp[i] = min(dp[i], dp[i-man] + cost)

print(min(dp[c:]))