import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    temp = int(input())
    if temp == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(temp), temp))