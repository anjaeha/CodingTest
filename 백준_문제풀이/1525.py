# 오른쪽 아래 가장 끝은 비어있다
# 인접해 있는 수를 그 칸으로 옮길 수 있다
# 최소의 이동으로 정리된 상태를 만드는 것이 목표
from collections import deque
graph = [list(map(int, input().split())) for _ in range(3)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


number = ''
for i in range(3):
    for j in range(3):
        number += str(graph[i][j])

q = deque()
q.append(number)

dist = dict()
dist[number] = 0

def bfs():
    while q:
        n = q.popleft()
        if n == '123456780':
            print(dist[n])
            return
        pos = n.index('0')
        x = pos // 3
        y = pos % 3

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                k = nx * 3 + ny
                ln = list(n)
                ln[k], ln[pos] = ln[pos], ln[k]
                ld = ''.join(ln)
                if not ld in dist:
                    dist[ld] = dist[n] + 1
                    q.append(ld)
    print(-1)

bfs()