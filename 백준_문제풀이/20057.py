# 그래프 밖으로 나간 모래의 양을 구하는 것이 문제

def solve(x, y, dir):
    global result

    lost_sand = 0
    
    for dx, dy, z in dir:
        nx = x + dx
        ny = y + dy

        if z == 0:
            new_sand = sand[x][y] - lost_sand
        else:
            new_sand = int(sand[x][y] * z)
            lost_sand += new_sand
        
        if 0 <= nx < n and 0 <= ny < n:
            sand[nx][ny] += new_sand
        else:
            result += new_sand



dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0] 
# 좌 하 우 상

n = int(input())
sand = [list(map(int, input().split())) for _ in range(n)]

c_x, c_y = n // 2, n // 2
result = 0

left = [(-1, 1, 0.01), (1, 1, 0.01), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05), (0, -1, 0)]
right = [[x, -y, z] for x, y, z in left]
up = [[y ,x,z] for x, y, z in left]
down = [[-y, x, z] for x, y, z in left]

dict = {0 : left, 1 : down, 2 : right, 3 : up}

for move in range(2 * n - 1):
    d = move % 4
    
    move_cnt = move // 2 + 1
    if move == 2 * n - 2:
        move_cnt -= 1
    
    for i in range(move_cnt):
        nx = c_x + dx[d]
        ny = c_y + dy[d]
        solve(nx, ny, dict[d])
        c_x, c_y = nx, ny

print(result)