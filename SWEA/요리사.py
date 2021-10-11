def make_candi(depth):
    global temp, candi
    if depth == n // 2:
        candi.append(list(temp))
        return

    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(i)
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, n):
            visit[j] = False

def make_1(depth, arr):
    global temp
    if depth == 2:
        food1_result.append(list(temp))
        return

    for i in range(n // 2):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(arr[i])
        make_1(depth + 1, arr)
        temp.pop()
        for j in range(i + 1, n // 2):
            visit[j] = False

def make_2(depth, arr):
    global temp
    if depth == 2:
        food2_result.append(list(temp))
        return

    for i in range(n // 2):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(arr[i])
        make_2(depth + 1, arr)
        temp.pop()
        for j in range(i + 1, n // 2):
            visit[j] = False

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    candi = []
    temp = []
    visit = [False] * n
    make_candi(0)
    result = 10000000
    for i in range(len(candi)):
        food1 = candi[i]
        food2 = []
        for j in range(n):
            if j not in food1:
                food2.append(j)
        food1_result = []
        food2_result = []
        visit = [False] * (n // 2)
        temp = []
        make_1(0, food1)
        
        visit = [False] * (n // 2)
        temp = []
        make_2(0, food2)

        one_point = 0
        for x, y in food1_result:
            one_point += graph[x][y]
            one_point += graph[y][x]
        
        two_point = 0
        for x, y in food2_result:
            two_point += graph[x][y]
            two_point += graph[y][x]
        
        result = min(result, abs(one_point - two_point))
    
    print("#%d %d" %(tc, result))