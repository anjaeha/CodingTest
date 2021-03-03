def solution(N, stages):
    result = {}
    num = len(stages)
    for stage in range(1, N+1):
        if num != 0:
            count = stages.count(stage)
            result[stage] = count / num
            num -= count
        else:
            result[stage] = 0
            
    return sorted(result, key = lambda x : -result[x])
    
print(solution(5, [2,1,2,6,2,4,3,3]))  