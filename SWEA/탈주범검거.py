from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dir = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]

T = int(input())

for tc in range(T):
    n, m, r, c, l = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    visit = [[False] * m for _ in range(n)]
    q = deque()
    q.append((r, c))
    visit[r][c] = True

    for idx in range(l - 1):
        new_q = deque()
        while q:
            x, y = q.popleft()
            for d in dir[graph[x][y]]:
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n and 0 <= ny < m:
                    if (d ^ 1) in dir[graph[nx][ny]]: # 반대로 돌아오는 길이 있어야함
                        if not visit[nx][ny] and graph[nx][ny]:
                            new_q.append((nx, ny))
                            visit[nx][ny] = True
        q = new_q

    result = 0
    for i in range(n):
        for j in range(m):
            if visit[i][j]:
                result += 1

    print("#%d %d" %(tc + 1, result))