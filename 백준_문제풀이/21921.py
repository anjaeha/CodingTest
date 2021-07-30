import sys
from collections import deque
input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))

answer = []
summary = 0
result = 0
q = deque()

for i in range(n):
    if len(q) < x:
        q.append(data[i])
        summary += data[i]
        result = summary
    else:
        q.append(data[i])
        summary -= q.popleft()
        summary += data[i]
        answer.append(result)
        result = summary

answer.append(result)

max_num = max(answer)

if max_num == 0:
    print('SAD')
else:
    print(max_num)
    print(answer.count(max_num))
