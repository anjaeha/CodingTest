def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnta = 0
    cntb = 0
    cntc = 0
    
    for i in range(len(answers)):
        if answers[i] == num1[i % len(num1)]:
            cnta += 1
        if answers[i] == num2[i % len(num2)]:
            cntb += 1
        if answers[i] == num3[i % len(num3)]:
            cntc += 1
    
    max_num = max(cnta, cntb, cntc)
    
    if max_num == cnta:
        answer.append(1)
    if max_num == cntb:
        answer.append(2)
    if max_num == cntc:
        answer.append(3)
        
    answer = sorted(answer)
    
    return answer