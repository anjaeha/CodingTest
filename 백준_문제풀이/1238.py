import heapq

n, m, k = map(int, input().split()) # N명의 학생, M개의 길, K번째에서 파티

graph = [[] for i in range(n + 1)]
for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

def djikstra(start):
    distance = [int(1e9)] * (n + 1)
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

    return distance

party = djikstra(k) # K에서 집으로 돌아가는 거리

MAX = -1
for i in range(1, n + 1):
    if i == k:
        continue

    dist = djikstra(i)
    MAX = max(MAX, party[i] + dist[k])

print(MAX)