import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


n = int(input())

board = [list(map(str, input().strip())) for _ in range(n)]
open = [list(map(str, input().strip())) for _ in range(n)]
count = [['.'] * n for _ in range(n)]



for i in range(n):
    for j in range(n):
        
        if open[i][j] == 'x' and board[i][j] == '.':
            cnt = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if board[nx][ny] == '*':
                    cnt += 1
            count[i][j] = cnt
        
        if board[i][j] == '*' and open[i][j] == 'x':
            Fail()

def Fail():
    global count
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                count[i][j] = '*'



for i in range(n):
    for j in range(n):
        print(count[i][j], end = '')
    print()