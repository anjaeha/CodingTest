def solution(sizes):
    right, left = [], []
    
    for x, y in sizes:
        right.append(max(x, y))
        left.append(min(x, y))
        
    right.sort()
    left.sort()
    
    return right[-1] * left[-1]