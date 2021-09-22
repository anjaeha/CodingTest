from copy import deepcopy

# 현재 상어의 위치 찾기
def shark_find(idx):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == idx:
                return (i, j)

# 상어 움직이기
def shark_move():
    global graph
    q = []
    s = [[0] * n for _ in range(n)]
    for idx in range(1, m + 1):
        d = shark_d[idx] # 현재 상어의 방향
        if d == 0: # 상어의 방향이 0이면 죽은 것이므로 진행할 필요가 없음.
            continue
        pos = shark_find(idx)
        x, y = pos[0], pos[1] # 현재 상어의 위치
        temp = priority_d[idx][d] # 현재 상어의 방향에서 우선순위 방향
        flag = True
        for i in range(1, 5):
            nx = x + dx[temp[i]]
            ny = y + dy[temp[i]]

            if 0 <= nx < n and 0 <= ny < n:
                if smell[nx][ny] == 0: # 냄새가 없는 칸으로 이동할 수 있게끔
                    if s[nx][ny]: # 겹치면 숫자가 작은 상어만 냄새 뿌릴수 있게 해줌.
                        if s[nx][ny] < idx: # 상어가 겹치면 작은 상어만 살아남음
                            shark_d[idx] = 0 # 상어가 나가면 방향을 0으로 바꿔서 1만 살아있는지 확인할수 있도록 함
                        else:
                            shark_d[s[nx][ny]] = 0 # 상어의 방향만 0으로 설정해줌.
                    s[nx][ny] = idx
                    q.append((nx, ny, idx, temp[i])) # 겹치는곳이 있는지 확인하고 smell에 넣어줌
                    flag = False
                    break
        
        # 4방향 중 냄새가 없는 방향이 없으면
        if flag:
            for i in range(1, 5):
                nx = x + dx[temp[i]]
                ny = y + dy[temp[i]]

                if 0 <= nx < n and 0 <= ny < n:
                    if smell[nx][ny][0] == idx: # 자신의 냄새가 있는 방향으로 감
                        shark_d[idx] = temp[i]
                        smell[nx][ny][1] = k
                        s[nx][ny] = idx
                        break
        
    for i in range(len(q)): # 상어가 새로 이동한 장소를 저장한 값중, 상어가 살아있을때만 값을 넣어줌.
        a, b, c, d = q[i]
        if shark_d[c] != 0:
            s[a][b] = c
            smell[a][b] = [c, k]
            shark_d[c] = d
        
    graph = deepcopy(s)

def first_smell():
    for idx in range(1, m + 1):
        pos = shark_find(idx)
        x, y = pos[0], pos[1] # 현재 상어의 위치
        smell[x][y] = [idx, k]

def spread_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j] != 0: # smell 이 0이 아니면 1을 빼주고, 0이 되면 0으로 초기화해줌.
                smell[i][j][1] -= 1
                if smell[i][j][1] == -1:
                    smell[i][j] = 0


n, m, k = map(int, input().split())
# n * n 격자에 m 마리의 상어, K초 후에 냄새 사라짐
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
# 위 아래 왼쪽 오른쪽

shark_d = [0] + list(map(int, input().split())) # 현재 상어의 방향

priority_d = [[]] # 상어 방향 우선순위
s = [[]]
for i in range(4 * m):    
    temp = [0] + list(map(int, input().split()))
    s.append((temp))
    if i % 4 == 3:
        priority_d.append(s)
        s = [[]]

smell = [[0] * n for _ in range(n)] # 냄새를 기억하기 위한 그래프
first_smell() # 첫번째 위치에 냄새를 뭍여줌
result = 0

while sum(shark_d[2:]) != 0 and result <= 1000:
    spread_smell()
    shark_move() # 상어 이동
    result += 1

print(result if result <= 1000 else -1)