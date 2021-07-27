import sys
from typing import overload
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0] * 1000001
max_x = 0

for i in range(n):
    g, x = map(int, input().split())
    arr[x] = g
    if x > max_x:
        max_x = x

q = deque()
result = 0
temp = 0

for i in range(max_x + 1):
    if len(q) < 2 * k + 1:
        temp += arr[i]
        q.append(arr[i])
        result = temp
    else:
        temp -= q.popleft()
        q.append(arr[i])
        temp += arr[i]
        if result < temp:
            result = temp

        
print(result)