def solution(lottos, win_nums):
    answer = []
    count = 0
    zeros = 0
    for lotto in lottos:
        if lotto in win_nums:
            count += 1
        if lotto == 0:
            zeros += 1
    
    answer = [count, count + zeros]

    grade = []
    for i in answer:
        if i >= 2:
            grade.append(7 - i)
        else:
            grade.append(6)
    grade.sort()
    return grade