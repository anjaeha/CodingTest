N, M = map(int, input().split())

s = [[0] * (N+1) for _ in range(N+1)]
visit = [0 for i in range(N+1)]
cnt = 0

#BFS 쓸거면 무조건 그래프 만들어주고 visit 0으로 하나 만들어주고, cnt 변수도 선언 해줘야 시작할수있다.


def dfs(i):
    visit[i] = 1
    for k in range(1, N+1):
        if s[i][k] == 1 and visit[k] == 0:
            dfs(k)


for case in range(M):
    a1, a2 = map(int, input().split())
    s[a1][a2] = 1
    s[a2][a1] = 1


for i in range(1, N+1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1
    
print(cnt)