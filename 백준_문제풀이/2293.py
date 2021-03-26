n, k = map(int, input().split())

c = []

for i in range(n):
    c.append(int(input()))

dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in c:
    for j in range(1, k+1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])