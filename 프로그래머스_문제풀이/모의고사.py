def solution(answers):
    answer = [[1,2,3,4,5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    corr = [0, 0, 0]
    for i in range(3):
        for ans in range(len(answers)):
            if answers[ans] == answer[i][ans % len(answer[i])]:
                corr[i] += 1
    
    result = []
    for i in range(3):
        if max(corr) == corr[i]:
            result.append(i + 1)
    return result