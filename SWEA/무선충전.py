T = int(input())

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

for tc in range(1, T + 1):
    m, a = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))

    graph = [[[(0,0)], [(0,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)]] for i in range(10)]

    for d in range(a):
        y, x, c, p = map(int, input().split())
        x, y = x - 1, y - 1
        for i in range(10):
            for j in range(10):
                if abs(x - i) + abs(y - j) <= c:
                    graph[i][j] += [(d + 1, p)]

    ax, ay = 0, 0
    bx, by = 9, 9
    result = 0

    for case in range(m + 1):
        order = sorted(graph[ax][ay], key = lambda x: -x[1]) # 현재 위치에서 충전 가능한 곳을 내림차순으로 받음
        order2 = sorted(graph[bx][by], key = lambda x: -x[1])
        a_max = order[0] # 현 위치에서 충전 최대치를 받아냄
        b_max = order2[0]

        if a_max[0] == b_max[0] and a_max[0] != 0: # 현 위치에서 충전 최대치가 같은 BC면
            a_sem = order[1] # 그 다음값을 받아냄
            b_sem = order2[1]

            if a_sem == b_sem == (0, 0): # 현 위치에 충전기가 하나라면 값을 더해주고
                result += a_max[1]
            else:
                result += (a_max[1] + max(a_sem[1], b_sem[1])) # 아니라면 최대값 + 그 다음 최대값값
        else:
            result += a_max[1] + b_max[1] # 같지않으면 두 최대값을 더해줌줌


        if case == m:
            break
        ax, ay = ax + dx[move_a[case]], ay + dy[move_a[case]] # 다음 위치로 이동
        bx, by = bx + dx[move_b[case]], by + dy[move_b[case]]

    print("#%d %d" %(tc, result))