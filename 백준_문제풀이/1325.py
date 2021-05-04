import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
s = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    s[y].append(x)

def bfs(start):
    q = deque()
    q.append(start)
    visit = [0] * (n+1)
    visit[start] = 1
    cnt = 1

    while q:
        x = q.popleft()
        for i in s[x]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                q.append(i)

    return cnt

result = []
max_cnt = 0

for i in range(1, n+1):
    temp = bfs(i)
    if max_cnt == temp:
        result.append(i)
    
    if max_cnt < temp:
        result = []
        max_cnt = temp
        result.append(i)


print(*result)