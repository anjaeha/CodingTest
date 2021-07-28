import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

summary, end, result = 0, 0, []
cnt = 0

for i in range(n):
    while summary < s and end < n:
        summary += data[end]
        end += 1
        cnt += 1
    
    if summary >= s:
        result.append(cnt)
    
    summary -= data[i]
    cnt -= 1

if result:
    print(min(result))
else:
    print(0)