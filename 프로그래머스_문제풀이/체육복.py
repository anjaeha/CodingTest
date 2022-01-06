def solution(n, lost, reserve):    
    # 본인에게 체육복이 있지만 도난당한 사람을 제외
    losts = []
    for i in lost:
        if i not in reserve:
            losts.append(i)
        else:
            reserve.remove(i)
            
    answer = n - len(losts)
    losts.sort()
    reserve.sort()
    for i in range(len(losts)):
        if (losts[i] - 1) in reserve:
            answer += 1
            reserve.remove(losts[i] - 1)
        elif (losts[i] + 1) in reserve:
            answer += 1
            reserve.remove(losts[i] + 1)
            
    return answer