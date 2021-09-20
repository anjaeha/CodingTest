
n = int(input())

# t = 1이면 x, y
# t = 2이면 x, y부터 오른쪽으로 붙어있는 타일
# t = 3이면 x, y부터 아래로 붙어있는 타일
tile = [list(map(int ,input().split())) for _ in range(n)]

graph = [[0] * 10 for _ in range(10)]
result = 0

def move_blue(t, x, y):
    if t == 1:
        while 0 <= y < 10 and graph[x][y] == 0:
            y += 1
        graph[x][y - 1] = 1
    elif t == 2:
        while 0 <= y < 10 and graph[x][y] == 0:
            y += 1
        graph[x][y - 1] = 1
        graph[x][y - 2] = 1
    elif t == 3:
        while 0 <= y < 10 and (graph[x][y] == 0 and graph[x + 1][y] == 0):
            y += 1
        graph[x][y - 1] = 1
        graph[x + 1][y - 1] = 1

def move_green(t, x, y):
    if t == 1:
        while 0 <= x < 10 and graph[x][y] == 0:
            x += 1
        graph[x - 1][y] = 1
    elif t == 2:
        while 0 <= x < 10 and (graph[x][y] == 0 and graph[x][y + 1] == 0):
            x += 1
        graph[x - 1][y] = 1
        graph[x - 1][y + 1] = 1
    elif t == 3:
        while 0 <= x < 10 and (graph[x][y] == 0):
            x += 1
        graph[x - 1][y] = 1
        graph[x - 2][y] = 1

def thick_check():
    global result
    # 진한 파란색 검사
    for i in range(6, 10):
        tmp = 0
        for j in range(4):
            if graph[j][i] == 1:
                tmp += 1
        if tmp == 4:
            s = [[0] * 10 for _ in range(10)]
            for x in range(10):
                for y in range(10):
                    s[y][x] = graph[x][y]
            
            s.pop(i)
            s.insert(4, [0] * 10)
            result += 1
            for x in range(10):
                for y in range(10):
                    graph[x][y] = s[y][x]
    
    # 진한 초록색 검사
    for i in range(6, 10):
        tmp = 0
        for j in range(4):
            if graph[i][j] == 1:
                tmp += 1
        if tmp == 4:
            graph.pop(i)
            graph.insert(4, [0] * 10)
            result += 1

def thin_check():
    global result

    for i in range(4, 6):
        tmp = 0
        for j in range(4):
            if graph[i][j] == 1:
                tmp += 1
        if tmp >= 1:
            graph.pop()
            graph.insert(4, [0] * 10)
    
    for i in range(4, 6):
        tmp = 0
        for j in range(4):
            if graph[j][i] == 1:
                tmp += 1
        if tmp >= 1:
            s = [[0] * 10 for _ in range(10)]
            for x in range(10):
                for y in range(10):
                    s[y][x] = graph[x][y]
            
            s.pop()
            s.insert(4, [0] * 10)
            for x in range(10):
                for y in range(10):
                    graph[x][y] = s[y][x]        


for i in tile:
    x, y, t = i
    move_blue(x, y, t)
    move_green(x, y, t)
    thick_check()
    thin_check()
    
answer = 0
for i in range(10):
    for j in range(10):
        if graph[i][j] == 1:
            answer += 1

print(result)
print(answer)