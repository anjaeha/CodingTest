# 약품에 도달하면 미생물 반죽고, 이동방향 반대로
# 두개 이상의 군집이 하나에 모이면, 합쳐지고, 이동방향은 가장 많은 군집을 따라감
# M시간 이후, 남아있는 미생물의 수 구하기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    n, m, k = map(int, input().split())

    cell = {}
    for i in range(k):
        x, y, size, dir = map(int, input().split())
        cell[(x, y)] = [(size, dir - 1)]

    for case in range(m):
        new_cell = {}
        flag = False
        for rc, val in cell.items():
            x, y = rc[0], rc[1]
            size, d = val[0][0], val[0][1]

            nx = x + dx[d]
            ny = y + dy[d]

            if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1:
                d ^= 1
                size = size // 2

            if new_cell.get((nx, ny)) is None:
                new_cell[(nx, ny)] = [(size, d)]
            else:
                flag = True
                new_cell[(nx, ny)].append((size, d))

        if flag:
            sum_cell = {}
            for rc, val in new_cell.items():
                if len(val) == 1:
                    sum_cell[rc[0], rc[1]] = val
                    continue
                sum_size = 0
                big_size = 0
                big_dir = 0

                for s, d in val:
                    sum_size += s
                    if big_size < s:
                        big_size = s
                        big_dir = d
                sum_cell[rc[0], rc[1]] = [(sum_size, big_dir)]
            cell = sum_cell
        else:
            cell = new_cell

    result = 0
    for rc, val in cell.items():
        result += val[0][0]
    print("#%d %d" % (tc, result))