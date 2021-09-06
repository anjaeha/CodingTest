def dfs(use_paper, cnt):
    global result
    if cnt == 0:
        if result > use_paper:
            result = use_paper
    elif use_paper >= result:
        return
    elif sum(paper) == 0:
        return
    
    for x in range(10):
        for y in range(10):
            if graph[x][y] == 1 and visit[x][y] == 0:
                for size in range(5, 0, -1):
                    if paper[size] > 0 and x + size <= 10 and y + size <= 10:
                        temp = 0
                        for nx in range(x, x + size):
                            for ny in range(y, y + size):
                                if visit[nx][ny] == 0:
                                    temp += graph[nx][ny]
                        if temp == size * size:
                            for nx in range(x, x + size):
                                for ny in range(y, y + size):
                                    visit[nx][ny] = 1
                            paper[size] -= 1
                            dfs(use_paper + 1, cnt - size * size)
                            for nx in range(x, x + size):
                                for ny in range(y, y + size):
                                    visit[nx][ny] = 0
                            paper[size] += 1

                return


graph = [list(map(int, input().split())) for _ in range(10)]
visit = [[0] * 10 for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]

one_cnt = 0
for i in range(10):
    for j in range(10):
        if graph[i][j] == 1:
            one_cnt += 1

if one_cnt == 0:
    print(0)
    exit()
elif one_cnt == 100:
    print(4)
    exit()

result = 26
dfs(0, one_cnt)

if result == 26:
    print(-1)
else:
    print(result)