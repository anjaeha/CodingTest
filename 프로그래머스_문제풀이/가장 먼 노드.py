from collections import deque


def solution(n, edge):
    def bfs():
        q = deque()
        q.append(1)

        while q:
            x = q.popleft()

            for i in graph[x]:
                if visit[i] == -1:
                    visit[i] = visit[x] + 1
                    q.append(i)

    visit = [-1] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    visit[1] = 0
    bfs()

    return visit.count(max(visit))