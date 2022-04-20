from collections import deque

def make_candi(depth):
    if depth == len(p_pos):
        candi.append(list(temp))
        return

    for i in range(2):
        temp.append(i)
        make_candi(depth + 1)
        temp.pop()

T = int(input())
for tc in range(T):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    p_pos = [] # 사람은 최대 10명
    s_pos = [] # 계단은 무조건 2개 (2 ~ 10의 길이를 가짐)
    s_time = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                p_pos.append((i, j))
            elif graph[i][j] > 1:
                s_pos.append((i, j))
                s_time.append(graph[i][j])

    up_x, up_y = s_pos[0]
    down_x, down_y = s_pos[1]
    temp = []
    candi = []
    make_candi(0)

    count = []
    for idx in range(len(candi)): # 해당 위치까지 이동하는데 얼마나 걸리는지 확인
        temp = []
        for now in range(len(p_pos)):
            if candi[idx][now] == 0:
                x = p_pos[now][0]
                y = p_pos[now][1]
                temp.append(abs(up_x - x) + abs(up_y - y))
            else:
                x = p_pos[now][0]
                y = p_pos[now][1]
                temp.append(abs(down_x - x) + abs(down_y - y))
        count.append(list(temp))

    result = int(1e9)
    for idx in range(len(candi)):
        pos = candi[idx] # 어디로 갈지 결정
        time = count[idx] # 계단까지 이동시간 결정

        up = [0, 0, 0] # 위 계단
        up_wait = deque()
        down = [0, 0, 0] # 아래 계단
        down_wait = deque()

        cnt = 0
        while 1:
            cnt += 1
            for i in range(3):
                if up[i] == 0:
                    continue
                if up[i][0] == 1:
                    up[i] = 0
                else:
                    up[i][0] -= 1

            for i in range(3):
                if down[i] == 0:
                    continue
                if down[i][0] == 1:
                    down[i] = 0
                else:
                    down[i][0] -= 1

            for i in range(3):
                if up[i] == 0 and up_wait:
                    up[i] = [s_time[0], up_wait.popleft()]
            for i in range(3):
                if down[i] == 0 and down_wait:
                    down[i] = [s_time[1], down_wait.popleft()]


            for now in range(len(time)):
                if time[now] == cnt:
                    if pos[now] == 0:
                        up_wait.append(now)
                    else:
                        down_wait.append(now)

            if cnt >= max(time) and not up_wait and not down_wait and up == [0, 0, 0] and down == [0, 0, 0] or result <= cnt:
                break

        result = min(result, cnt)

    print("#%d %d" %(tc + 1, result))