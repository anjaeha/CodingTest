import heapq
import sys
input = sys.stdin.readline

n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
room.sort(key = lambda x : x[0])
end = []

for s, e in room:
    if end:
        if end[0] <= s:
            heapq.heappop(end)
    heapq.heappush(end, e)

print(len(end))