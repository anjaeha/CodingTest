import heapq, sys

v, e, p = map(int, input().split())
INF = sys.maxsize
start = 1

graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstart(start, end):
    distance = [INF] * (v + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]

if dijkstart(1, v) == dijkstart(1, p) + dijkstart(p, v):
    print("SAVE HIM")
else:
    print("GOOD BYE")