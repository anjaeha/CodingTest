n = int(input())
graph = [[0] * 101 for _ in range(101)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
# 동, 북, 서, 남

for _ in range(n):
    y, x, d, g = map(int, input().split())
    # (y, x)좌표, 시작방향, 세대가 주어짐
    graph[x][y] = 1
    move = [d]

    for _ in range(g):
        q = []
        for i in range(len(move)):
            q.append((move[-1-i] + 1) % 4) # 3세대면 2세대 + 1세대 + 0세대가 이어짐을 알 수 있다.
        move.extend(q)
    
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        graph[nx][ny] = 1
        x, y = nx, ny

result = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]:
            if graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
                result += 1

print(result)