from itertools import permutations

def calc(op, cnt, exp):
    if exp.isdigit():
        return exp
    else:
        if op[cnt] == '*':
            split_data = exp.split('*')
            temp = []
            for s in split_data:
                temp.append(calc(op, cnt + 1, s))
            return str(eval('*'.join(temp)))
        if op[cnt] == '+':
            split_data = exp.split('+')
            temp = []
            for s in split_data:
                temp.append(calc(op, cnt + 1, s))
            return str(eval('+'.join(temp)))
        if op[cnt] == '-':
            split_data = exp.split('-')
            temp = []
            for s in split_data:
                temp.append(calc(op, cnt + 1, s))
            return str(eval('-'.join(temp)))

def solution(expression):
    answer = 0
    ops = list(permutations(['-', '*', '+'], 3))
    
    for op in ops:
        result = abs(int(calc(op, 0, expression)))
        
        if result > answer:
            answer = result
    
    return answer