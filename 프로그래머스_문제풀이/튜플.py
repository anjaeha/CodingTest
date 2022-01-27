from collections import Counter
def solution(s):
    s = s.replace('{', '').replace('}', '').replace(',', ' ')
    s = s.split()
    
    answer = []
    s = sorted(Counter(s).items(), key = lambda x : x[1])
    
    for rc, val in s:
        answer.append(int(rc))
        
    return answer[::-1]