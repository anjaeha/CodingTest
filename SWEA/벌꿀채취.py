def make_candi(x, y): # 가능한 경우의 수 구하기
    answer = []
    if y + m > n:
        return
    
    for i in range(0, y + m):
        visit[x][i] = True
    
    for i in range(x, n):
        for j in range(n):
            temp = []
            if j + m > n:
                break
            for k in range(m):
                if not visit[i][j + k]:
                    temp.append(graph[i][j + k])
                else:
                    break
            if len(temp) == m:
                answer.append(temp)
    answer_xy = []
    for i in range(m):
        answer_xy.append(graph[x][y + i])
    return answer_xy, answer # (answer_xy)일때 가능한 좌표 answer

def honey_count(arr): # 꿀로 얻을 수 있는 최대의 수익 구하기
    arr.sort()
    answer = -1
    for cnt in range(m): # 가장 큰 수 하나보다 다른 수의 합이 더 클 수 있음.
        temp = 0
        avb = c
        for i in range(len(arr) - cnt - 1, -1, -1):
            if arr[i] <= avb:
                temp += arr[i] ** 2
                avb -= arr[i]
        answer = max(answer, temp)
    return answer

T = int(input())

for case in range(T):
    n, m, c = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = -1
    candiA = []
    candiB = []
    
    # A의 위치가 정해졌을 때, B의 경우의 수를 구함.
    for i in range(n):
        for j in range(n):
            visit = [[False] * n for _ in range(n)]
            if j + m > n:
                continue
            temp_a, temp_b = make_candi(i, j)
            if temp_a and temp_b:
                candiA.append(temp_a)
                candiB.append(temp_b)
    
    for idx in range(len(candiA)):
        this_a = candiA[idx]
        this_b = candiB[idx]

        max_a = honey_count(this_a)
        max_b = -1
        for i in range(len(this_b)):
            temp = honey_count(this_b[i])
            max_b = max(temp, max_b)
        
        result = max(result, max_a + max_b)        
    print("#%d %d" %(case + 1, result))