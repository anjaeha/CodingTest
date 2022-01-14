from itertools import permutations
def solution(k, dungeons):
    cnt = [i for i in range(len(dungeons))]
    candi = list(permutations(cnt, len(dungeons)))
    
    answer = 0
    
    for order in candi:
        tired = k
        count = 0
        for i in order:
            if tired >= dungeons[i][0]:
                count += 1
                tired -= dungeons[i][1]
            else:
                break
                
        answer = max(answer, count)
        
    return answer