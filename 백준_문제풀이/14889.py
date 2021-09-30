n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
member = n // 2

candi_team = []
temp = []
visit = [False] * n
# 팀 나눌수 있는 경우의 수 구하기
def div_team(depth):
    global temp
    if depth == member:
        candi_team.append(list(temp))
        return
    
    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(i)
        div_team(depth + 1)
        temp.pop()
        for j in range(i + 1, n):
            visit[j] = False
div_team(0)

MIN = 1000
for i in range(len(candi_team)):
    Ateam = candi_team[i]
    Bteam = []
    for i in range(n):
        if i not in Ateam:
            Bteam.append(i)
    A = 0
    B = 0
    for i in Ateam:
        for j in Ateam:
            A += graph[i][j]
    for i in Bteam:
        for j in Bteam:
            B += graph[i][j]
    MIN = min(MIN, abs(A - B))
    
print(MIN)