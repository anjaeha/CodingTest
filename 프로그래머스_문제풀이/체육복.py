def solution(n, lost, reserve):
    number = [1] * (n+1)
    number[0] = 0
    
    for i in lost:
        number[i] -= 1
    for i in reserve:
        number[i] += 1
    
    for i in range(1, n):
        if number[i] == 0:
            if number[i-1] == 2:
                number[i-1] = 1
                number[i] = 1
            elif number[i+1] == 2:
                number[i+1] = 1
                number[i] = 1
    cnt = 0
    for i in number:
        if i >= 1:
            cnt += 1
    
    
    return cnt