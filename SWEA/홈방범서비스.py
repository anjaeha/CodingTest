T = int(input())
for case in range(T):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    house = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                house.append((i, j))
    
    max_cost = len(house) * m # 모든 집이 서비스를 받을때 얻는 수익
    result = 0
    for k in range(n + 2): # 그래프의 크기가 N이면, N + 1크기의 마름모가 있어야 모든 범위를 커버할 수 있다.
        cost = k * k + (k - 1) * (k - 1)
        if max_cost - cost > 0: # 손해를 보면 할 필요가 없음.
            for i in range(n):
                for j in range(n): # k크기의 마름모를 모든 지점에서 탐색한다.
                    cnt = 0 # 서비스를 받는 집의 숫자
                    for x, y in house:
                        dist = abs(x - i) + abs(y - j) # 집의 위치와 마름모 중심까지의 거리를 구해서
                        if dist < k: # 마름모의 크기보다 작으면 마름모 안에 있는 것으로 판단
                            cnt += 1
                    if result < cnt and m * cnt - cost >= 0: # 더 많은 집이 서비스를 받고, 손해를 보지 않으면 result 값 갱신해줌.
                        result = cnt
    print("#%d %d" %(case + 1, result))