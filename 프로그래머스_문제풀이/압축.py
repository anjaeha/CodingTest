def solution(msg):
    answer = []
    alpha = {}
    for i in range(65, 91):
        alpha[chr(i)] = i - 64
    
    idx = 0
    long = 0
    maxidx = 26
    
    while 1:
        long += 1
        if msg[idx : idx + long] not in alpha:
            maxidx += 1
            alpha[msg[idx : idx + long]] = maxidx
            answer.append(alpha[msg[idx : idx + long - 1]])
            idx += long - 1
            long = 0
        else:
            if idx + long - 1 == len(msg):
                answer.append(alpha[msg[idx : idx + long - 1]])
                break
                
    return answer