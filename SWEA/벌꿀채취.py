# N * N크기의 벌통
# 두 명의 일꾼은 M개가 가로로 연속되도록 선택하여 벌을 채취함.
def make_candi(x, y):
    for i in range(0, y + m):
        visit[x][i] = True
    a = []
    for i in range(m):
        a.append(graph[x][y + i])

    b = []
    for i in range(x, n):
        for j in range(n):
            if visit[i][j] or j + m > n:
                continue
            temp = []
            for k in range(m):
                temp.append(graph[i][j + k])
            b.append(list(temp))
    return a, b

def honey_count(arr):
    arr.sort()
    answer = 0
    for i in range(m):
        avg = c
        temp = 0
        for j in range(m - 1 - i, - 1, -1):
            if arr[j] <= avg:
                avg -= arr[j]
                temp += arr[j] ** 2
        answer = max(temp, answer)
    return answer


T = int(input())

for tc in range(1, T + 1):
    n, m, c = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    candi_A = []
    candi_B = []
    result = -1

    for i in range(n):
        for j in range(n):
            visit = [[False] * n for _ in range(n)]
            if j + m > n:
                continue
            tempa, tempb = make_candi(i, j)
            if tempa and tempb:
                candi_A.append(tempa)
                candi_B.append(tempb)

    for i in range(len(candi_A)):
        for j in range(len(candi_B[i])):
            before = candi_A[i]
            after = candi_B[i][j]

            max_b = honey_count(before)
            max_a = honey_count(after)

            result = max(result, max_a + max_b)

    print("#%d %d" %(tc, result))