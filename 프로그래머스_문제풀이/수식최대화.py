from itertools import permutations
def solution(expression):
    answer = -1
    temp = ''
    expre = []
    for i in range(len(expression)):
        if expression[i].isdigit():
            temp += expression[i]
        else:
            expre.append(temp)
            expre.append(expression[i])
            temp = ''
    expre.append(temp)
    
    calc = ['*', '-', '+']
    priority = list(permutations(calc, len(calc)))
    
    for p in priority:
        temp = expre[:]
        for i in range(len(p)):
            while p[i] in temp:
                idx = temp.index(p[i])
                t = temp[idx - 1] + temp[idx] + temp[idx + 1]
                del temp[idx - 1], temp[idx - 1], temp[idx - 1]
                temp.insert(idx - 1, str(eval(t)))
        
        if len(temp) == 1:
            answer = max(answer, abs(int(temp[0])))
    
    return answer