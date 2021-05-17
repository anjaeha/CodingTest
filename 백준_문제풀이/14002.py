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

idx = max(dp)
cnt = dp.index(idx)
arr = []

while cnt >= 0:
    if dp[cnt] == idx:
        arr.append(s[cnt])
        idx -= 1

    cnt -= 1

print(max(dp))
print(*arr[::-1])