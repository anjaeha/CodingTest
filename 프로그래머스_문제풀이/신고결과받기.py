def solution(id_list, report, k):
    answer = []
    report = list(set(report)) # 신고 내역 중복제거
    
    ID = {}
    
    for i in report: # 몇번 신고 받았는지를 확인
        x, y = i.split()
        if y in ID:
            ID[y] += 1
        else:
            ID[y] = 1
    
    pause = [] # 정지당한사람 구하기
    for rc, val in ID.items():
        if val >= k:
            pause.append(rc)
            
    result = {} # 몇명 정지시켰는지 구하기
    for i in report:
        x, y = i.split()
        if y in pause:
            if x in result:
                result[x] += 1
            else:
                result[x] = 1
    
    for i in id_list:
        if i in result:
            answer.append(result[i])
        else:
            answer.append(0)
            
    return answer