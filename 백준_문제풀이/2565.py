n = int(input())
l = []
l_ = []
dp = [0 for _ in range(n)]

for i in range(n):
    l.append(list(map(int, input().split())))
l.sort(key = lambda x : x[0])

for i in range(n):
    l_.append(l[i][1])

for i in range(n):
    for j in range(i):
        if l_[i] > l_[j] and dp[i] < dp[j]:
            dp[i] = dp[j]

    dp[i] += 1


print(n - max(dp))