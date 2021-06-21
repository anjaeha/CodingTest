def solution(dartResult):
    answer = 0
    number = []
    
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == '1' and dartResult[i+1] == '0':
                number.append(10)
            elif dartResult[i] == '0' and dartResult[i-1] == '1':
                continue
            else:
                number.append(int(dartResult[i]))
        else:
            if dartResult[i] == 'D':
                number[-1] = number[-1] ** 2
            elif dartResult[i] == 'T':
                number[-1] = number[-1] ** 3
            elif dartResult[i] == '*':
                if len(number) == 1:
                    number[-1] = number[-1] * 2
                else:
                    number[-1] = number[-1] * 2
                    number[-2] = number[-2] * 2
            elif dartResult[i] == '#':
                    number[-1] = number[-1] * (-1)
                    
    return sum(number)