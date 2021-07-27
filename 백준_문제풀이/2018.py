import sys
input = sys.stdin.readline

n = int(input())
data = [i for i in range(1, n+1)]

summary, end, result = 0, 0, 0

for i in range(n):

    while summary < n and end < n:
        summary += data[end]
        end += 1

    if summary == n:
        result += 1
    
    summary -= data[i]

print(result)