from collections import deque
def dfs(x):
    global answer
    visit[x] = True
    for i in graph[x]:
        if not visit[i]:
            dfs(i)
            answer += 1
"""
def bfs(x):
    visit[x] = True
    answer = 0
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visit[i]:
                q.append(i)
                answer += 1
                visit[i] = True
    return answer
"""
n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결되어 잇는 컴퓨터 쌍의 수
graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visit = [False] * (n + 1)
answer = 0
dfs(1) # bfs(1)로도 가능하다

print(answer)