import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))

answer = 0
for i in range(1, m-1):
    left = s[:i]
    right = s[i+1:]

    height = min(max(left), max(right))

    temp = height - s[i]
    if temp > 0:
        answer += temp
        
print(answer)