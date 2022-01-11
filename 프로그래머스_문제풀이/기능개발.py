def solution(p, s):
    answer = []
    
    while p:
        for i in range(len(p)):
            p[i] += s[i]
        
        cnt = 0
        while p and p[0] >= 100:
            p.pop(0)
            s.pop(0)
            cnt += 1
        if cnt:
            answer.append(cnt)
    return answer