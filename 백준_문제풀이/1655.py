import heapq
import sys
input = sys.stdin.readline

n = int(input())
mid = int(input())
left = []
right = []
print(mid)
for _ in range(1, n):
    temp = int(input())
    if temp > mid:
        heapq.heappush(right, temp)
        if len(left) + 1 < len(right):
            heapq.heappush(left, (-mid, mid))
            mid = heapq.heappop(right)
    else:
        heapq.heappush(left, (-temp, temp))
        if len(right) < len(left):
            heapq.heappush(right, mid)
            mid = heapq.heappop(left)[1]
    print(mid)