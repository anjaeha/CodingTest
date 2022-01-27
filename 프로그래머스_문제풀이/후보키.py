# 각 col별로 중복되는게 잇는지 확인, 있다면 있는거끼리 후보키 만들기
from itertools import combinations
def solution(relation):
    answer = 0
    count = [i for i in range(len(relation[0]))]
    length = len(relation)
    candi = []
    for i in range(1, len(relation[0]) + 1):
        candi += (list(combinations(count, i)))
    
    result = []
    for c in candi:
        temp = ['' for _ in range(length)]
        for i in c:
            for j in range(length):
                temp[j] += relation[j][i]
        if len(set(temp)) == length:
            temp = ''
            for i in c:
                temp += str(i)
            result.append(temp)
    
    sol = []
    for res in result:
        flag = True
        
        if not sol:
            sol.append(res)
            continue
        for s in sol:
            cnt = 0
            for i in s:
                if i in res:
                    cnt += 1
            if cnt == len(s):
                flag = False

        if flag:
            sol.append(res)
    
    return len(sol)