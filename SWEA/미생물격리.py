dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 상, 하, 좌, 우

def calc(dict):
    total = 0
    for rc, val in dict.items():
        total += val[0]
    return total

def move():
    global virus
    for _ in range(m):
        new = {}
        for rc, val in virus.items():
            num, dir, _ = val
            nx = rc[0] + dx[dir]
            ny = rc[1] + dy[dir]

            # 미생물 군집의 위치가 테두리면 크기를 2로 나눠주고 방향을 변경한다.
            if nx == 0 or nx == n -1 or ny == 0 or ny == n - 1:
                dir ^= 1
                num //= 2
            
            if (nx, ny) not in new:
                new[(nx, ny)] = [num, dir, num]
            else: # 미생물 군집의 위치가 겹치면 최대값을 비교하여준다.
                if num > new[(nx, ny)][2]:
                    new[(nx, ny)][1] = dir
                    new[(nx, ny)][2] = num
                new[(nx, ny)][0] += num
            
            virus = new
        
    return calc(virus)

T = int(input())

for case in range(T):
    n, m, k = map(int, input().split())
    # 크기 N, 격리 시간 M, 군집의 수 K
    virus = {}
    for i in range(k):
        x, y, size, dir = map(int, input().split())
        virus[(x, y)] = [size, dir - 1, size]
    
    print("#%d %d" %(case + 1, move()))