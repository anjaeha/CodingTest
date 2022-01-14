def solution(citations):
    answer = 0
    for i in range(1, len(citations) + 1):
        cnt = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                cnt += 1
        if cnt >= i:
            answer = i
        else:
            break
            
    return answer