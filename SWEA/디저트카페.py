from collections import deque

T = int(input())

dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]

def search(sx, sy):
    global result
    visit = [graph[sx][sy]]
    q = deque()
    q.append((sx, sy, 0, visit))
    answer = 0
    while q:
        x, y, cnt, visit = q.popleft()

        if cnt > 3:
            continue

        nx = x + dx[cnt]
        ny = y + dy[cnt]

        if (nx, ny) == (sx, sy) and cnt == 3:
            answer = max(answer, len(visit))
            continue
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] not in visit:
                visit.append(graph[nx][ny])
                q.append((nx, ny, cnt + 1, visit[:]))
                q.append((nx, ny, cnt, visit[:]))
    return answer

for tc in range(T):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    result = -1
    for x in range(n):
        for y in range(n):
            temp = search(x, y)
            result = max(result, temp)

    print("#%d %d" %(tc + 1, result if result != 0 else -1))