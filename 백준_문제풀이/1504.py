import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())



def djikstra(start):
    distance = [int(1e9)] * (n + 1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist < distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

# 1번 -> v1 -> v2 -> n
# 1번 -> v2 -> v1 -> n 이렇게 2가지 경우의 수를 구해서 비교해야함.

distance_start = djikstra(1) # 1번에서 다른 정점으로 까지의 최단경로
distance_v1 = djikstra(v1) # v1에서 다른 정점으로 까지의 최단경로
distance_v2 = djikstra(v2) # v2에서 다른 정점으로 까지의 최단경로

answer1 = distance_start[v1] + distance_v1[v2] + distance_v2[n]
answer2 = distance_start[v2] + distance_v2[v1] + distance_v1[n]

result = min(answer1, answer2)
if result >= int(1e9):
    print(-1)
else:
    print(result)