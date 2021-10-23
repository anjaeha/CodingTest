# 10 * 10크기의 그래프, 사용자는 2명, (0,0) (9,9)에서 시작함.

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    n, a = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))
    graph = [[[(0, 0)] for _ in range(10)] for _ in range(10)]

    for case in range(a):
        y, x, c, p = map(int, input().split()) # (x, y)에 충전범위, 성능
        x, y = x - 1, y - 1
        for i in range(10):
            for j in range(10):
                if abs(i - x) + abs(j - y) <= c:
                    if graph[i][j] == 0:
                        graph[i][j] = [case + 1, p]
                    else:
                        graph[i][j].append((case + 1, p))
    ax, ay = 0, 0
    result_a = [graph[ax][ay]]
    for i in range(n):
        ax = ax + dx[move_a[i]]
        ay = ay + dy[move_a[i]]
        result_a.append(graph[ax][ay])

    bx, by = 9, 9
    result_b = [graph[bx][by]]
    for i in range(n):
        bx = bx + dx[move_b[i]]
        by = by + dy[move_b[i]]
        result_b.append(graph[bx][by])

    result = 0
    for i in range(n + 1):
        cura = result_a[i]
        curb = result_b[i]
        cura.sort(key = lambda x: -x[1])
        curb.sort(key = lambda x: -x[1])

        if len(cura) == len(curb) == 1:
            continue

        if cura[0][0] == curb[0][0]:
            result += cura[0][1]
            result += max(cura[1][1], curb[1][1])
        else:
            result += cura[0][1] + curb[0][1]

    print("#%d %d" %(tc, result))