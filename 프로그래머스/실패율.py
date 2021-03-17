from collections import Counter

def solution(N, stages):
    answer = []

    avg = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        avg[i] = (stages.count(i) / len(stages))
        while i in stages:
            stages.remove(i)
    avg.pop(0)

    idx = [i for i in range(1, N+1)]
    avgIndex = list(zip(avg, idx))
    
    avgIndex.sort(key = lambda x : -x[0])
    
    for k in range(N):
        answer.append(avgIndex[k][1])

    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))  
# 37점..