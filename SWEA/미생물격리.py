dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    n, m, k = map(int, input().split())  # N * N 크기, M 시간후, K개의 미생물
    pos = {}
    for _ in range(k):
        x, y, s, d = map(int, input().split())  # 좌표, 미생물 수, 이동방향
        pos[x, y] = [s, d - 1]

    for idx in range(m):
        new_pos = {}
        for rc, val in pos.items():
            r, c, s, d = rc[0], rc[1], val[0], val[1]
            x = r + dx[d]
            y = c + dy[d]
            if x == 0 or x == n - 1 or y == 0 or y == n - 1:
                new_pos[x, y] = [[s // 2, d ^ 1]]
            else:
                if (x, y) in new_pos:
                    new_pos[x, y].append([s, d])
                else:
                    new_pos[x, y] = [[s, d]]

        pos = {}
        for rc, val in new_pos.items():
            if len(val) > 1:  # 두개 이상이 뭉치면
                max_size, total_size, d = 0, 0, -1  # 최대 크기, 크기의 총합, 방향
                for size, dir in val:
                    total_size += size
                    if max_size < size:
                        max_size = size
                        d = dir
                a = val
                pos[rc[0], rc[1]] = [total_size, d]
            else:
                a = rc
                b = val
                pos[rc[0], rc[1]] = [val[0][0], val[0][1]]

    result = 0
    for rc, val in pos.items():
        result += val[0]

    print("#%d %d" % (tc + 1, result))