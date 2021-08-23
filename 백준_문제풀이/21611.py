import sys
input = sys.stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

sdx = [0, 1, 0, -1]
sdy = [-1, 0, 1, 0]

result = 0

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]

mid_x, mid_y = n // 2, n // 2
graph[mid_x][mid_y] = 9
ans1, ans2, ans3 = 0, 0, 0
def move_snail(array):
    x, y = n // 2, n // 2
    for i in range(n * 2 - 1):
        for k in range(i // 2 + 1):
            try:
                nx = x + sdx[i % 4]
                ny = y + sdy[i % 4]
                if 0 <= nx < n and 0 <= ny < n:
                    graph[nx][ny] = array.pop(0)
                    x, y = nx, ny
            except:
                break

def boom(dir, dis):
    x, y = n // 2, n // 2
    for i in range(dis):
        nx = x + dx[dir]
        ny = y + dy[dir]
        graph[nx][ny] = 0
        x, y = nx, ny

def search():
    global ans1, ans2, ans3
    global result
    arr = []
    x, y = n // 2, n // 2
    for i in range(n * 2 - 1):
        for k in range(i // 2 + 1):
            nx = x + sdx[i % 4] 
            ny = y + sdy[i % 4]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 0:
                    arr.append(graph[nx][ny])
                x, y = nx, ny

    while 1:
        flag = False
        number = 0
        count = []
        color = []
        for i in range(len(arr)):
            if number == arr[i]:
                count.append(count.pop() + 1)
            else:
                number = arr[i]
                count.append(1)
                color.append(number)

        cnt = 0
        for i in range(len(count)):
            if count[i] >= 4:
                flag = True
                array = arr[:cnt] + arr[cnt+count[i]:]
                idx = count[i]
                boomColor = color[i]

                if boomColor == 1:
                    result += count[i]
                    ans1 += count[i]
                elif boomColor == 2:
                    result += count[i] * 2
                    ans2 += count[i]
                elif boomColor == 3:
                    result += count[i] * 3
                    ans3 += count[i]
                arr = array
            else:
                cnt += count[i]

        if not flag:
            break
    
    count = []
    color = []
    answer = []
    number = 0
    for i in range(len(arr)):
        if number == arr[i]:
            count.append(count.pop() + 1)
        else:
            number = arr[i]
            count.append(1)
            color.append(number)

    for i in range(len(count)):
        answer.append(count[i])
        answer.append(color[i])

    return answer

for case in range(m):
    dir, dis = move[case]
    boom(dir, dis)
    q = search()
    graph  = [[0] * n for _ in range(n)]
    move_snail(q)
    graph[n // 2][n // 2] = 9

print(result)
