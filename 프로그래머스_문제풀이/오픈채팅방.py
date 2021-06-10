id = dict()
def solution(record):
    answer = []
    logList = []
    
    for e in record:
        dataList = e.split(" ")
        if dataList[0] == 'Leave':
            logList.append([dataList[1], "님이 나갔습니다."])
        elif dataList[0] == 'Enter':
            id[dataList[1]] = dataList[2]
            logList.append([dataList[1], "님이 들어왔습니다."])
        elif dataList[0] == 'Change':
            id[dataList[1]] = dataList[2]


    for log in logList:
        answer.append(id[log[0]] + log[1])
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))