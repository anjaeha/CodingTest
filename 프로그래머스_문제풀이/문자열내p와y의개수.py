def solution(s):
    answer = True
    s = s.lower()
    
    p_cnt = s.count('p')
    y_cnt = s.count('y')
    
    
    return True if p_cnt == y_cnt else False