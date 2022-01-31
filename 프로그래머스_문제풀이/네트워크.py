from collections import deque


def solution(n, cs):
    network = [[] for _ in range(n)]
    visit = [-1] * n
    for x in range(n):
        for y in range(n):
            if x == y:
                continue
            if cs[x][y] == 1:
                network[x].append(y)
                network[y].append(x)

    def bfs(x, idx):
        q = deque()
        q.append(x)
        visit[x] = idx
        while q:
            x = q.popleft()

            for i in network[x]:
                if visit[i] == -1:
                    visit[i] = idx
                    q.append(i)

    idx = 1
    for i in range(n):
        if visit[i] == -1:
            bfs(i, idx)
            idx += 1

    return len(set(visit))