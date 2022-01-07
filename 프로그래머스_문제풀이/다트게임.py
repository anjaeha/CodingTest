def solution(dartResult):
    answer = []
    result = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == '1' and dartResult[i + 1] == '0':
                answer.append(10)
            elif dartResult[i] == '0' and dartResult[i - 1] == '1':
                continue
            else:
                answer.append(int(dartResult[i]))
        else:
            if dartResult[i] == 'S':
                answer[-1] = answer[-1] ** 1
            elif dartResult[i] == 'D':
                answer[-1] = answer[-1] ** 2
            elif dartResult[i] == 'T':
                answer[-1] = answer[-1] ** 3
            elif dartResult[i] == '*':
                answer[-1] *= 2
                if len(answer) > 1:
                    answer[-2] *= 2
            elif dartResult[i] == '#':
                answer[-1] *= -1
                
    return sum(answer)