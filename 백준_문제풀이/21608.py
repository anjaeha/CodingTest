import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
favorite = [[]]

for _ in range(n**2):
    cnt, a, b, c, d = map(int, input().split())
    favorite.append((cnt, a, b, c, d))


classRoom = [[0] * n for _ in range(n)]


for i in range(1, n ** 2 + 1):
    temp = []
    for x in range(n):
        for y in range(n):
            zero = 0
            friend = 0
            
            if classRoom[x][y] == 0:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if classRoom[nx][ny] == 0:
                            zero += 1
                        if classRoom[nx][ny] in favorite[i][1:]:
                            friend += 1
    
            temp.append((friend, zero, x, y))
    temp.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    for kk in range(n ** 2):
        if not classRoom[temp[kk][2]][temp[kk][3]]:
            classRoom[temp[kk][2]][temp[kk][3]] = favorite[i][0]
            break


result = 0

favor = favorite[1:]
favor.sort(key = lambda x : x[0])

for x in range(n):
    for y in range(n):
        num = classRoom[x][y]
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if classRoom[nx][ny] in favor[num - 1][1:]:
                    cnt += 1

        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result)