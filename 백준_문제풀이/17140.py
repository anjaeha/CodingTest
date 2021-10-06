# R 연산 - 행을 정렬, 행의 개수 >= 열의 개수인 경우에 적용
# C 연산 - 열을 정렬, 행의 개수 < 열의 개수인 경우에 적용
# 연산을 적용하고 가장 큰 배열의 길이에 맞춰 0으로 채움 (0은 정렬할때 무시)
# 크기가 100을 넘어가면 버리기

r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]
# graph[r][c] == k가 되는 최소 연산 시간 구하기 (100초 넘으면 - 1)

def calC():
    s = [[0] * len(graph) for _ in range(len(graph[0]))]
    for i in range(len(graph[0])):
        for j in range(len(graph)):
              s[i][j] = graph[j][i]
    MAX = 0
    for i in range(len(s)):
        arr = s[i]
        s[i] = []
        temp = {}
        for j in arr:
            if j != 0:
                if j in temp:
                    temp[j] += 1
                else:
                    temp[j] = 1        
        temp = sorted(temp.items(), key = lambda x : (x[1], x[0]))
        for rc, val in temp:
            s[i].append(rc)
            s[i].append(val)
        MAX = max(MAX, len(s[i]))
    
    for i in range(len(s)):
        while len(s[i]) != MAX:
            s[i].append(0)

    answer = [[0] * len(s) for _ in range(len(s[0]))]
    for i in range(len(s)):
        for j in range(len(s[0])):
            answer[j][i] = s[i][j]
    return answer

def calR():
    s = [[] for _ in range(len(graph))]
    MAX = 0
    for i in range(len(s)):
        arr = graph[i]
        temp = {}
        for j in arr:
            if j != 0:
                if j in temp:
                    temp[j] += 1
                else:
                    temp[j] = 1        
        temp = sorted(temp.items(), key = lambda x : (x[1], x[0]))
        for rc, val in temp:
            s[i].append(rc)
            s[i].append(val)
        MAX = max(MAX, len(s[i]))
    
    for i in range(len(s)):
        while len(s[i]) != MAX:
            s[i].append(0)
    return s

cnt = 0
while cnt <= 100:
    if len(graph) >= r and len(graph[0]) >= c:
        if graph[r - 1][c - 1] == k:
            break
    if len(graph) >= len(graph[0]):
        graph = calR()
    else:
        graph = calC()

    cnt += 1

print(cnt if cnt != 101  else -1)