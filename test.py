def solution(dartResult):
    answer = []
    count = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            answer.append(count)
            count = int(dartResult[i])
        else:
            if dartResult[i] == 'S':
                count = count ** 1
            elif dartResult[i] == 'D':
                count = count ** 2
            elif dartResult[i] == 'T':
                count = count ** 3
            elif dartResult[i] == '*':
                count *= 2
                answer[-1] *= 2
            elif dartResult[i] == '#':
                count *= -1
    
    answer.append(count)
    print(answer)
    return sum(answer)