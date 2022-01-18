def solution(n, left, right):
    answer = []
    
    for idx in range(left, right + 1):
        q, r = idx // n, idx % n
        answer.append(max(q, r) + 1)
    
    return answer