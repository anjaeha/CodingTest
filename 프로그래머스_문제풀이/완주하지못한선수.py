from collections import Counter

def solution(p, c):
    result = Counter(p) - Counter(c)
    
    return list(result)[0]