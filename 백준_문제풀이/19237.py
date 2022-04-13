n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
shark_dir = [0] + list(map(int, input().split()))
dir = [[]] + [[[0]] + [list(map(int, input().split())) for _ in range(4)] for _ in range(m)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

smell = [[0] * n for _ in range(n)]
pos = {}
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            pos[graph[i][j]] = (i, j)
            graph[i][j] = 0

def spread(): # 냄새 뿌리기
    for idx in range(1, m + 1):
        if idx in pos:
            x, y = pos[idx]
            smell[x][y] = [idx, k]

def shark_move(): # 상어 움직이기
    for idx in range(1, m + 1):
        if idx in pos:
            x, y = pos[idx]
            temp = shark_dir[idx] # 현재 방향에서 우선순위

            for d in dir[idx][temp]:
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n and 0 <= ny < n:
                    if smell[nx][ny] == 0:
                        pos[idx] = (nx, ny)
                        shark_dir[idx] = d
                        break
            else:
                for d in dir[idx][temp]:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == idx:
                            pos[idx] = (nx, ny)
                            shark_dir[idx] = d
                            break
    for idx in range(1, m + 1): # 겹칠경우 제외해주기
        if idx in pos:
            for j in range(idx + 1, m + 1):
                if j in pos:
                    if pos[idx] == pos[j]:
                        del pos[j]

def smell_down(): # 냄새 1 감소
    for i in range(n):
        for j in range(n):
            if smell[i][j]:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = 0

def check(): # 1을 제외한 다른 상어가 남아있는지 확인
    for idx in range(2, m + 1):
        if idx in pos:
            return False
    return True

result = 0
while 1:
    if check() or result > 1000:
        break
    result += 1
    spread()
    shark_move()
    smell_down()

print(result if result != 1001 else -1)