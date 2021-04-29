import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))

dp = []

for i in range(n-1):
    dp.append(s[i+1] - s[i])

dp.sort()
print(sum(dp[:n-k]))