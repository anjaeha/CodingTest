import heapq
import sys
input = sys.stdin.readline

n = int(input())

q = []
for i in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(q, (-x, x))
    else:
        if q == []:
            print(0)
        else:
            print(heapq.heappop(q)[1])