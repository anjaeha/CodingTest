def solution(table, languages, preference):
    work = []
    work_at = []
    for i in range(len(table)):
        temp = table[i].split()
        work_at.append(temp[0])
        work.append((temp[1:]))
        
    

    grade = []
    for i in range(len(work)):
        count = 0
        for j in range(len(languages)):
            if languages[j] in work[i]:
                temp = 5 - work[i].index(languages[j])
                temp *= preference[j]
            else:
                temp = 0
            count += temp
        grade.append(count)
        
            
    answer = list(zip(grade, work_at))
    answer.sort(key = lambda x : (-x[0], x[1]))
    
    return answer[0][1]