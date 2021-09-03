import sys
from heapq import heappush, heappop
input = sys.stdin.readline

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

n, m = map(int, input().split())

array = [[] for _ in range(n + 1)]
INF = sys.maxsize


for _ in range(m):
    a, b, c = map(int, input().split())
    array[a].append((b, c))
    array[b].append((a, c))


v1 ,v2 = map(int, input().split())

# 1번 -> v1 -> v2 -> n
# 1번 -> v2 -> v1 -> n 이렇게 2가지 경우의 수를 구해서 비교해야함.

distance_start = djikstra(1) # 1번에서 다른 정점으로 까지의 최단경로
distance_v1 = djikstra(v1) # v1에서 다른 정점으로 까지의 최단경로
distance_v2 = djikstra(v2) # v2에서 다른 정점으로 까지의 최단경로

answer1 = distance_start[v1] + distance_v1[v2] + distance_v2[n]
answer2 = distance_start[v2] + distance_v2[v1] + distance_v1[n]

result = min(answer1, answer2)
if result >= INF:
    print(-1)
else:
    print(result)