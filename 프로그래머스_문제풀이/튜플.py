def solution(s):
    answer = []
    s = s[2:-2]
    
    ans = s.split("},{")
    
    for i in ans:
        n = i.split(',')
        
        for j in n:
            if int(j) not in answer:
                answer.append(int(j))

    return answer
    
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))