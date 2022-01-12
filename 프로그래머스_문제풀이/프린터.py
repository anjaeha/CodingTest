def solution(p, location):
    check = [False] * len(p)
    check[location] = True
    answer = 0
    
    while 1:
        if p[0] == max(p):
            p.pop(0)
            temp = check.pop(0)
            answer += 1
            if temp == True:
                return answer
        else:
            p.append(p.pop(0))
            check.append(check.pop(0))