r, c, m = map(int, input().split())

# 0, 위, 아래, 오른쪽, 왼쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

fish = {}
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    fish[x - 1, y - 1] = [s, d - 1, z] # 속력, 이동방향, 크기

def fish_move():
    global fish
    new_fish = {}
    for rc, val in fish.items():
        x, y, s, d, z = rc[0], rc[1], val[0], val[1], val[2]
        if d == 0 or d == 1:  # 상 하 일때 최종 몇번 움직여야하는지 계산해줌
            s = s % (r * 2 - 2)
        elif d == 2 or d == 3: # 좌 우 일때
            s = s % (c * 2 - 2)
        for i in range(s):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= r or ny < 0 or ny >= c: # 벽에 부딪히면
                d ^= 1 # 방향 반대로 바꾸고 다시 한칸 이동해줌
                nx = x + dx[d]
                ny = y + dy[d]
            x, y = nx, ny
        if (x, y) in new_fish:
            if new_fish[x, y][2] > z:
                continue
            else:
                new_fish[x, y] = [s, d, z]
        else:
            new_fish[x, y] = [s, d, z]

    fish = new_fish

# 낚시, 상어이동 순서로 진행
result = 0
for tc in range(c):
    for i in range(r):
        if (i, tc) in fish:
            result += fish[i, tc][2] # 크기 더해주고
            del fish[i, tc]
            break
    fish_move()

print(result)