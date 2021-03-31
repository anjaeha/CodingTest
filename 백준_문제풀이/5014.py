from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

s_ = [-1 for _ in range(f)]
s_[s - 1] = 0
dire = [u, -d]
visit = [0 for _ in range(f)]

def bfs(i):
    q = deque()
    q.append(i)
    visit[i] = 1
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + dire[i]

            if 0 <= nx < f and visit[nx] == 0:
                q.append(nx)
                s_[nx] = s_[x] + 1
                visit[nx] = 1

bfs(s - 1)
print(s_[g - 1] if s_[g - 1] != -1 else "use the stairs")
