
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, board):
    visit = [[False] * n for _ in range(n)]
    visit[x][y] = True
    
    q = deque()
    q.append((x, y, 1))
    answer = [(x, y, 1)]

    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny] and board[x][y] > board[nx][ny]:
                    answer.append((nx, ny, cnt + 1))
                    q.append((nx, ny, cnt + 1))
    answer.sort(key = lambda x : -x[2])
    return answer[0][2]

T = int(input())
for case in range(1, T + 1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    highest = []
    MAX = -1
    for i in range(n):
        for j in range(n):
            MAX = max(MAX, graph[i][j])
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == MAX:
                highest.append((i, j))
    
    result = -1
    for i in range(n):
        for j in range(n):
            copy_graph = [item[:] for item in graph]
            for c in range(k):
                if copy_graph[i][j] > 0:
                    copy_graph[i][j] -= 1
                for x, y in highest:
                    temp = move(x, y, copy_graph)
                    result = max(result, temp)

    print("#%d %d" %(case, result))