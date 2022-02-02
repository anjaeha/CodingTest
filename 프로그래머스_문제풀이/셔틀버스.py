from collections import deque

# 09시부터 n회 운행, 간격T(분), 최대인원M
def solution(n, t, m, timetable):
    minutes = []
    for i in timetable:
        minutes.append(int(i[:2]) * 60 + int(i[3:5]))
    minutes.sort()
    minutes = deque(minutes)

    bus_time = deque([540])
    for i in range(n - 1):
        bus_time.append(bus_time[-1] + t)

    for i in range(n - 1):
        for j in range(m):
            if bus_time and minutes:
                if bus_time[0] >= minutes[0]:
                    minutes.popleft()
        bus_time.popleft()

    people = []
    for i in minutes:
        if bus_time[0] + 1 > i:
            people.append(i)

    if not people:
        answer = bus_time[0]
    else:
        if len(people) < m:
            answer = bus_time[0]
        else:
            answer = people[m - 1] - 1

    left, right = str(answer // 60), str(answer % 60)

    result = left.zfill(2) + ':' + right.zfill(2)

    return result