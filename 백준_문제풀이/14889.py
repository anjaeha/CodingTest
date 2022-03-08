n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

numbers = [i for i in range(n)]
team_A = []
team_B = []
temp = []
visit = [False] * n

def make_candi(depth):
    global temp
    if depth == n // 2:
        team_A.append(list(temp))
        tt = []
        for i in range(n):
            if i not in temp:
                tt.append(i)
        team_B.append(list(tt))

    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(i)
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, n):
            visit[j] = False
make_candi(0)

answer = int(1e9)

for i in range(len(team_A)):
    temp_A = team_A[i]
    temp_B = team_B[i]

    SUM_A = 0
    SUM_B = 0

    for i in range(len(temp_A)):
        for j in range(len(temp_A)):
            SUM_A += graph[temp_A[i]][temp_A[j]]
            SUM_B += graph[temp_B[i]][temp_B[j]]
    answer = min(answer, abs(SUM_A - SUM_B))

print(answer)