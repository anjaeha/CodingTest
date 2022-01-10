def solution(s):
    up = []
    low = []
    
    for i in s:
        if i.isupper():
            up.append(i)
        else:
            low.append(i)
            
    low.sort(reverse = True)
    up.sort(reverse = True)
    
    answer = ''
    for i in low:
        answer += i
    for i in up:
        answer += i
        
    return answer


def solution(s):
    s = list(s)
    s.sort(reverse = True)
    
    return ''.join(s)