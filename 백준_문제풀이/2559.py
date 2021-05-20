import sys
input = sys.stdin.readline

n, k = map(int, input().split())

s = list(map(int, input().split()))

tmp = sum(s[:k])
result = tmp

for i in range(k, n):
    tmp += s[i] - s[i-k]
    result = max(result, tmp)

print(result)