from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(arr, x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= len(arr) or ny >= len(arr[0]):
                continue
                
            if arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
    
def solution(maps):
    bfs(maps, 0, 0)
    if maps[len(maps) - 1][len(maps[0]) - 1] == 1:
        return -1
    else:
        return maps[len(maps) - 1][len(maps[0]) - 1]


# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))