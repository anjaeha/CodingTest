import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0] * 1000001

max_x = 0
for i in range(n):
    g, x = map(int, input().split())
    arr[x] = g
    if max_x < x:
        max_x = x

q = deque()
temp = 0
result = 0

for i in range(max_x + 1):
    if len(q) < 2 * k + 1:
        q.append(arr[i])
        temp += arr[i]
        result = temp
    else:
        temp -= q.popleft()
        q.append(arr[i])
        temp += arr[i]

        if result < temp:
            result = temp

print(result)