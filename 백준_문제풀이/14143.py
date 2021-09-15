from copy import deepcopy
# 낚시
def catch(idx):
    global result
    for i in range(n):
        if graph[i][idx]:
            temp = graph[i][idx].pop()
            result += temp[2]
            return

# 상어이동
def shark_move():
    s = [[[] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                x = deepcopy(i)
                y = deepcopy(j)
                temp = list(graph[x][y].pop())
                for _ in range(temp[0]):
                    nx = x + dx[temp[1]]
                    ny = y + dy[temp[1]]
					# 허용된 범위 안에서 움직이면 패스
                    if 0 <= nx < n and 0 <= ny < m:
                        pass
                    else:
                    	# 0번방향을 1로, 1번 방향을 2로 변경하며
                        # 2번 방향을 3으로, 3번 방향을 2로 변경한다. 2진법에서 1의 자리 숫자 변경하는 효과
                        temp[1] ^= 1
                        if nx < 0:
                            nx = -nx
                        elif ny < 0:
                            ny = -ny
                        elif nx >= n:
                            nx = n - 2
                        elif ny >= m:
                            ny = m - 2
                    x, y = nx, ny
                # 만약에 비어있으면 그대로 저장
                if not s[x][y]:
                    s[x][y].append((temp[0], temp[1], temp[2]))
                # 이미 값이 저장되어있으면 크기 비교해서 큰 상어를 넣어준다.
                else:
                    if s[x][y][0][2] > temp[2]:
                        pass
                    else:
                        s[x][y].pop()
                        s[x][y].append((temp[0], temp[1], temp[2]))

    return s

n, m, c = map(int, input().split())
if c == 0:
    print(0)
    exit()
graph = [[[] for _ in range(m)] for _ in range(n)]

shark = []
for _ in range(c):
    # 좌표, 속도, 이동방향, 크기
    x, y, s, d, z = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    graph[x][y].append((s, d, z))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
# 상, 하, 우, 좌

result = 0

for i in range(m):
    catch(i)
    s = shark_move()
    graph = deepcopy(s)

print(result)