def solution(N, stages):
    player = len(stages)
    rate = [[i, 0] for i in range(N + 1)]
    
    for i in range(1, N + 1):
        # 현재 i단계에 위치한 사람의 수 구하기
        pos = stages.count(i)
        if player == 0:
            continue
        rate[i] = [i, pos / player]
        player -= pos
    
    rate.sort(key = lambda x : (-x[1], x[0]))
    answer = []
    for i in range(len(rate)):
        answer.append(rate[i][0])
    
    answer.remove(0)
    return answer