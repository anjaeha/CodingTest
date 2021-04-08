import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())

    if x == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))