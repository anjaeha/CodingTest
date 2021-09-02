import sys
from heapq import heappop, heappush
n = int(input())
m = int(input())

array = [[] for _ in range(n + 1)]
INF = sys.maxsize
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    array[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    distance[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue

        for i in array[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))


dijkstra(start)
print(distance[end])

