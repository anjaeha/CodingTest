# 바이러스는 상하좌우로 모든칸으로 동시복제
# M개를 활성 상태로 변경
# 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간
# 빈칸 - 0, 벽 - 1, 바이러스 - 2
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus_pos = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus_pos.append((i, j))

candi = []
visit = [False] * len(virus_pos)
temp = []
def make_candi(depth):
    if depth == m:
        candi.append(list(temp))
        return

    for i in range(len(virus_pos)):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(virus_pos[i])
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, len(virus_pos)):
            visit[j] = False

make_candi(0) # 활성화되는 경우의 수

def spread(arr):
    board = [[-1] * n for _ in range(n)]
    q = deque()
    visit = [[False] * n for _ in range(n)]
    for x, y in arr:
        q.append((x, y))
        visit[x][y] = True
        board[x][y] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 1 and not visit[nx][ny]: # 벽이 아니고 방문하지 않았을 때
                    board[nx][ny] = board[x][y] + 1
                    visit[nx][ny] = True
                    q.append((nx, ny))

    # 몇초 걸렸는지 출력
    result = -1
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                if not visit[i][j]: # 벽이 아닌데, 방문하지 않았으면 False 출력 => 실패한 경우
                    return False
                result = max(result, board[i][j])
    return result

MIN = int(1e9)

for idx in range(len(candi)):
    temp = spread(candi[idx])
    if temp == False: # False값이 오면 패스
        continue

    if temp == -1:
        MIN = 0
        break
    MIN = min(MIN, temp)

    if MIN == 0:
        break

if MIN == int(1e9):
    print(-1)
else:
    print(MIN)