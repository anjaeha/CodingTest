from itertools import combinations_with_replacement
def solution(n, info):
    ret = [-1] * 12
    for combi in combinations_with_replacement(range(11), n):

        arrow = [0] * 12
        score = 0
        
        for i in combi:
            arrow[i] += 1
        
        for i in range(11):
            if arrow[i] > info[i]:
                score += (10 - i)
            elif info[i] != 0:
                score -= (10 - i)
        
        if score <= 0:
            continue
        arrow[11] = score
        if arrow[::-1] > ret[::-1]:
            ret = arrow[:]
    
    if ret[0] == -1:
        return [-1]
    return ret[:-1]