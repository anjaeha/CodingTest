def solution(msg):
    answer = []
    alpha = dict()
    for i in range(ord('A'), ord('Z') + 1):
        alpha[chr(i)] = i - 64
        
    idx = 0
    leng = 0
    maxidx = 26
    
    while 1:
        leng += 1
        if not msg[idx:idx+leng] in alpha:
            maxidx += 1
            alpha[msg[idx:idx+leng]] = maxidx
            answer.append(alpha[msg[idx:idx+leng-1]])
            idx = idx + leng - 1
            leng = 0
        else:
            if idx + leng - 1 == len(msg):
                answer.append(alpha[msg[idx:idx+leng-1]])
                break
                
    return answer