# 가로 W 세로 D
# 세로방향으로 K개 이상이 있어야 통과
# A를 B로 바꿀수 있고 B를 A로 바꿀 수 있음. 한줄을A로, 한줄을B로 가능

def make_candi(depth, cnt):
    global temp, candi
    if depth == cnt:
        candi.append(list(temp))

    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(i)
        make_candi(depth + 1, cnt)
        temp.pop()
        for j in range(i + 1, n):
            visit[j] = False

def check(graph):
    for i in range(m):
        flag = False
        temp = 1
        color = -1
        for j in range(n):
            if color == graph[j][i]:
                temp += 1
                if temp >= k:
                    flag = True
                    break
            else:
                temp = 1
                if temp >= k:
                    flag = True
                    break
                color = graph[j][i]
        if not flag:
            return False
    return True

T = int(input())

for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)] # 0이면 A 1이면 B
    copy_graph = [item[:] for item in graph]
    candi = [] # 용액을 붓는 경우의 수 구하기, A를 부을 수도 있고, B를 부을 수도 있고, AB모두 부을 수도 있음
    for idx in range(n + 1):
        visit = [False] * n
        temp = []
        make_candi(0, idx)
    result = 987654321
    flag = False
    for idx in range(len(candi)):
        cur = candi[idx]
        for c in range(len(cur)):
            for i in range(m):
                copy_graph[cur[c]][i] = 0
        temp = check(copy_graph)
        if temp:
            result = len(cur)
            flag = True
            break
        for c in range(len(cur)):
            for i in range(m):
                copy_graph[cur[c]][i] = 1
        temp = check(copy_graph)
        if temp:
            result = len(cur)
            flag = True
            break

        for c in range(len(cur) // 2):
            for i in range(m):
                copy_graph[cur[c]][i] = 0
        for c in range(len(cur) // 2, len(cur)):
            for i in range(m):
                copy_graph[cur[c]][i] = 1
        temp = check(copy_graph)
        if temp:
            result = len(cur)
            flag = True
            break
        for c in range(len(cur) // 2):
            for i in range(m):
                copy_graph[cur[c]][i] = 1
        for c in range(len(cur) // 2, len(cur)):
            for i in range(m):
                copy_graph[cur[c]][i] = 0
        temp = check(copy_graph)
        if temp:
            result = len(cur)
            flag = True
            break

        copy_graph = [item[:] for item in graph]

    print("#%d %d" %(tc, result))