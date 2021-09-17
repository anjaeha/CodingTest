from copy import deepcopy

n, m, t = map(int, input().split())
graph = [[0] * m]
graph += [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(t)]

# 돌리는 배열의 x + 1값과 x값 x - 1을 확인하여 연속되는 수가 있으면 지우고, y값을 확인해서 그것도 지움
# d가 0이면 시계, 1이면 반시계
for case in range(t):
    x, d, k = move[case]
    # 배열 돌리기
    for i in range(1, n + 1):
        if i % x == 0:
            if d == 0: # 시계는 N번이 1번으로
                for j in range(k):
                    graph[i].insert(0, graph[i].pop())
            elif d == 1: # 반시계는 1번이 N번으로
                for j in range(k):
                    graph[i].append(graph[i].pop(0))
    
    # 인접한 곳에 숫자가 같은지 확인
    s = [[0] * m for _ in range(n + 1)]
    for i in range(1, n + 1): # x값
        for j in range(m): # y값
            if graph[i][j] != 0:
                if i == 1:
                    if j < m - 1:
                        if graph[i][j] == graph[i][j - 1] or graph[i][j] == graph[i][j + 1] or graph[i][j] == graph[i + 1][j]:
                            s[i][j] = 0
                        else:
                            s[i][j] = graph[i][j]
                    else:
                        if graph[i][j] == graph[i][j - 1] or graph[i][j] == graph[i][0] or graph[i][j] == graph[i + 1][j]:
                            s[i][j] = 0
                        else:
                            s[i][j] = graph[i][j]
                elif 1 < i < n:
                    if j < m - 1:
                        if graph[i][j] == graph[i][j - 1] or graph[i][j] == graph[i][j + 1] or graph[i][j] == graph[i + 1][j] or graph[i][j] == graph[i - 1][j]:
                            s[i][j] = 0
                        else:
                            s[i][j] = graph[i][j]
                    else:
                        if graph[i][j] == graph[i][j - 1] or graph[i][j] == graph[i][0] or graph[i][j] == graph[i + 1][j] or graph[i][j] == graph[i - 1][j]:
                            s[i][j] = 0
                        else:
                            s[i][j] = graph[i][j]
                elif i == n:
                    if j < m - 1:
                        if graph[i][j] == graph[i][j - 1] or graph[i][j] == graph[i][j + 1] or graph[i][j] == graph[i - 1][j]:
                            s[i][j] = 0
                        else:
                            s[i][j] = graph[i][j]
                    else:
                        if graph[i][j] == graph[i][j - 1] or graph[i][j] == graph[i][0] or graph[i][j] == graph[i - 1][j]:
                            s[i][j] = 0
                        else:
                            s[i][j] = graph[i][j]
    
    # 만약에 중복된게 없으면 평균구해서 +- 1을 해줌
    if graph == s:
        temp = 0
        cnt = 0
        for i in range(1, n + 1):
            for j in range(m):
                if graph[i][j] != 0:
                    temp += graph[i][j]
                    cnt += 1
        # 만약에 합이 0이면 끝내줌
        if temp == 0:
            break
        temp = temp / cnt
        for i in range(1, n + 1):
            for j in range(m):
                if graph[i][j] != 0:
                    if graph[i][j] > temp:
                        graph[i][j] -= 1
                    elif graph[i][j] < temp:
                        graph[i][j] += 1
    else:
        graph = deepcopy(s)
    

result = 0
for i in range(1, n + 1):
    for j in range(m):
        result += graph[i][j]
print(result)