import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, m, x = map(int, input().split())
array = [[] for _ in range(n + 1)]
INF = sys.maxsize


for _ in range(m):
    a, b, c = map(int, input().split())
    array[a].append((b, c))

def djikstra(start):
    distance = [INF] * (n + 1)
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
    return distance

start_x = djikstra(x)

MAX = -1
for i in range(1, n + 1):
    if i == x:
        continue
    temp = 0
    dis = djikstra(i)
    temp += start_x[i] + dis[x]
    MAX = max(MAX, temp)

print(MAX)