from itertools import combinations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(arr):
    visit = [[False] * 5 for _ in range(5)]
    x, y = arr[0][0], arr[0][1]
    visit[x][y] = True
    q = deque()
    q.append((x, y))
    count = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 5 and 0 <= ny < 5:
                if not visit[nx][ny] and (nx, ny) in arr:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                    count += 1

    if count == 7:
        return True
    else:
        return False

graph = [list(input()) for _ in range(5)]
numbers = [i for i in range(25)]
candi = list(combinations(numbers, 7))

answer = 0

for idx in candi:
    temp = []
    for i in idx:
        temp.append((i // 5, i % 5))

    if not check(temp):
        continue

    cnt_s = 0
    cnt_y = 0
    for i in temp:
        x, y = i
        if graph[x][y] == 'Y':
            cnt_y += 1
        else:
            cnt_s += 1

    if cnt_s >= 4:
        answer += 1

print(answer)