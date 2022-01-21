from math import ceil
def solution(fees, records):
    period = {}
    parking = {}
    for record in records:
        time, car, act = record.split()
        h, m = time.split(":")
        
        if act == 'IN':
            parking[car] = int(h) * 60 + int(m) # 분으로 저장
        else:
            if car in period:
                period[car] += int(h) * 60 + int(m) - parking[car]
            else:
                period[car] = int(h) * 60 + int(m) - parking[car]
            del parking[car]
    
    
    if parking:
        for rc, val in parking.items():
            if rc in period:
                period[rc] += 1439 - val
            else:
                period[rc] = 1439 - val
            
    # fees [기본 시간, 기본 요금, 단위 시간, 단위 요금]
    cost = {}
    for rc, val in period.items():
        if val <= fees[0]:
            cost[rc] = fees[1]
        else:
            cost[rc] = ceil((val - fees[0]) / fees[2]) * fees[3] + fees[1]
    
    cost = sorted(cost.items(), key = lambda x : x[0])
    answer = []
    
    for rc, val in cost:
        answer.append(val)
        
    return answer