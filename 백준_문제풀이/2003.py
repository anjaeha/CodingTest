import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

summary = 0
end = 0
result = 0

for i in range(n):
    while summary < k and end < n:
        summary += data[end]
        end += 1

    if summary == k:
        result += 1

    summary -= data[i]

print(result)