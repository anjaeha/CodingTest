T = int(input())

temp = []
def make_candi(depth, idx):
    global temp
    if depth == idx:
        temp_use1 = []
        temp_use2 = []
        for i in range(1, len(p_pos) + 1):
            if i not in temp:
                temp_use2.append(i)
            else:
                temp_use1.append(i)
        use1.append(temp_use1)
        use2.append(temp_use2)
        return

    
    for i in range(len(p_pos)):
        if visit[i]:
            continue

        visit[i] = True
        temp.append(people[i])
        make_candi(depth + 1, idx)
        temp.pop()
        for j in range(i + 1, len(p_pos)):
            visit[j] = False


for case in range(T):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    p_pos = [] # 사람의 위치
    s_pos = [] # 계단의 위치
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                p_pos.append((i, j))
            elif graph[i][j] >= 2:
                s_pos.append((i, j, graph[i][j]))

    # 1번계단과 2번계단을 사용하는 경우의 수를 모두 구함.
    use1 = []
    use2 = []
    people = [i for i in range(1, len(p_pos) + 1)]
    for idx in range(len(p_pos) + 1):
        visit = [False] * len(p_pos)
        make_candi(0, idx)

    
    result = 100000000
    for idx in range(len(use1)): # 모든 경우의 수를 직접 해봄
        t = 0
        cnt_done = 0
        s1 = [[0, 0] for _ in range(3)] # 1번 계단을 이용한 시간
        s2 = [[0, 0] for _ in range(3)] # 2번 게단을 이용한 시간
        candi1 = [] # 1번 계단을 기다리는 사람
        candi2 = [] # 2번 계단을 기다리는 사람
        u1 = use1[idx]
        u2 = use2[idx]
        while cnt_done < len(p_pos): # 모든 사람이 내려가기 전까지 반복함
            if t >= result:
                break

            s1x, s1y = s_pos[0][0], s_pos[0][1] # 계단에 도착하면 대기열에 넣어줌
            remove_u1 = []
            for i in range(len(u1)):
                x, y = p_pos[u1[i] - 1][0], p_pos[u1[i] - 1][1]
                absx, absy = abs(s1x - x), abs(s1y - y)
                if absx + absy == t:
                    candi1.append(u1[i])


            s2x, s2y = s_pos[1][0], s_pos[1][1]
            for i in range(len(u2)):
                x, y = p_pos[u2[i] - 1][0], p_pos[u2[i] - 1][1]
                absx, absy = abs(s2x - x), abs(s2y - y)
                if absx + absy == t:
                    candi2.append(u2[i])


            for i in range(3): # 계단을 모두 내려가면 초기화해주고 자리를 비워줌
                if s1[i][1]:
                    if t - s1[i][1] == s_pos[0][2]:
                        cnt_done += 1
                        s1[i] = [0, 0]
            
            for i in range(3):
                if s2[i][1]:
                    if t - s2[i][1] == s_pos[1][2]:
                        cnt_done += 1
                        s2[i] = [0, 0]

            # 계단을 기다리고 있는 사람이 있으면 빈자리가 나면 사용함
            for i in range(3):
                if s1[i][0] == 0 and candi1:
                    s1[i] = [candi1.pop(0), t]

            for i in range(3):
                if s2[i][0] == 0 and candi2:
                    s2[i] = [candi2.pop(0), t]
            
            
            t += 1
        if result > t:
            result = t
    print("#%d %d" %(case + 1, result))


"""
# 계단에는 최대 3명 올라갈 수 있음.

def make_candi(depth, cnt):
    if depth == cnt:
        candi.append(list(temp))
        return

    for i in range(len(p)):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(i)
        make_candi(depth + 1, cnt)
        temp.pop()
        for j in range(i + 1, len(p)):
            visit[j] = False

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 987654321
    p = []
    s = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                p.append((i, j))
            elif 2 <= graph[i][j] <= 10:
                s.append((i, j))
    sp1 = graph[s[0][0]][s[0][1]]
    sp2 = graph[s[1][0]][s[1][1]]
    # 계단은 2개, 사람의 수는 1 ~ 10
    candi = []
    for i in range(len(p) + 1):
        visit = [False] * len(p)
        temp = []
        make_candi(0, i)

    for case in range(len(candi)):
        stair1 = candi[case]
        stair2 = []
        for idx in range(len(p)):
            if idx not in stair1:
                stair2.append(idx)

        stair1_use = [0, 0, 0]
        stair2_use = [0, 0, 0]
        stair1_wait = []
        stair2_wait = []

        for s1 in range(len(stair1)):
            px, py = p[stair1[s1]]
            stair1_wait.append((p[stair1[s1]], abs(px - s[0][0]) + abs(py - s[0][1])))
        for s2 in range(len(stair2)):
            px, py = p[stair2[s2]]
            stair2_wait.append((p[stair2[s2]], abs(px - s[1][0]) + abs(py - s[1][1])))

        stair1_wait.sort(key = lambda x : x[1])
        stair2_wait.sort(key = lambda x : x[1])

        cnt = 0
        cnt_done = 0
        while cnt_done < len(p):
            cnt += 1
            for j in range(3):
                if stair1_use[j] == 0:
                    continue
                if stair1_use[j] + sp1 == cnt:
                    cnt_done += 1
                    stair1_use[j] = 0
            for j in range(3):
                if stair2_use[j] == 0:
                    continue
                if stair2_use[j] + sp2 == cnt:
                    cnt_done += 1
                    stair2_use[j] = 0

            for j in range(3):
                if stair1_wait and stair1_use[j] == 0:
                    if stair1_wait[0][1] + 1 <= cnt:
                        cur = stair1_wait.pop(0)
                        stair1_use[j] = cnt

            for j in range(3):
                if stair2_wait and stair2_use[j] == 0:
                    if stair2_wait[0][1] + 1 <= cnt:
                        cur = stair2_wait.pop(0)
                        stair2_use[j] = cnt

        result = min(result, cnt)
    print("#%d %d" %(tc, result))
"""