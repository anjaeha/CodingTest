import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = [list(map(str, input().strip())) for _ in range(12)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit = [[0] * 6 for _ in range(12)]
    visit[x][y] = 1
    boom = [[x, y]]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6:
                if board[x][y] == board[nx][ny] and visit[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = 1
                    boom.append((nx, ny))
    if len(boom) >= 4:
        for a, b in boom:
            board[a][b] = '.'

    return len(boom)

def fall():  #밑으로 내리기. 밑에서부터 저장하고 밑에서부터 순서대로 입력해줌. 어차피 밑에 다 깔림.
    for j in range(6):
        bag = deque()
        for i in range(11, -1, -1):
            if board[i][j] != '.':
                bag.append(board[i][j])
        
        for i in range(11, -1, -1):
            if bag:
                board[i][j] = bag.popleft()
            else:
                board[i][j] = '.'


answer = 0

while 1:
    count = 0
    # count 변수 만들어서 4개이상 터진적이 있는지 확인.
    # 여러 그룹이 터지더라도 한번의 연쇄가 추가됨. 모았다가 answer 1회 증가.
    for i in range(12):
        for j in range(6):
            cnt = 0
            if board[i][j] != '.':
                cnt = bfs(i, j)
                if cnt >= 4:
                    count += cnt

    if count == 0:
        break
    if count >= 4:
        answer += 1
    fall()

            
print(answer)