import heapq
import sys
input = sys.stdin.readline

n = int(input())
one = int(input())
s = []

for i in range(n-1):
    temp = int(input())
    heapq.heappush(s, (-temp, temp))

cnt = 0
while s:
    temp = heapq.heappop(s)[1]
    if one > temp:
        break
    else:
        cnt += 1
        one += 1
        temp -= 1
        heapq.heappush(s, (-(temp), temp))
print(cnt)