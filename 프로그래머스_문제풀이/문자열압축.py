def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s) // 2 + 1):
        cnt = 1
        tmp = s[:i]
        word = ''
        
        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt == 1:
                    word = word + tmp
                else:
                    word = word + str(cnt) + tmp
                cnt = 1
                tmp = s[j : i + j]
        if cnt == 1:
                word = word + tmp
        else:
            word = word + str(cnt) + tmp
        answer.append(len(word))
        
    return min(answer)