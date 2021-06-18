def solution(lottos, win_nums):
    cnt = 0
    zero = 0
    answer = []
    for i in lottos:
        if i in win_nums:
            cnt += 1
        if i == 0:
            zero += 1
    
    if zero + cnt == 6:
        answer.append(1)
    elif zero + cnt == 5:
        answer.append(2)
    elif zero + cnt == 4:
        answer.append(3)
    elif zero + cnt == 3:
        answer.append(4)
    elif zero + cnt == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if cnt == 6:
        answer.append(1)
    elif cnt == 5:
        answer.append(2)
    elif cnt == 4:
        answer.append(3)
    elif cnt == 3:
        answer.append(4)
    elif cnt == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    return answer