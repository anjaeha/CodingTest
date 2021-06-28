def solution(dirs):

    d = {'U' : 0, 'D' : 1, 'R' : 2, 'L' : 3}
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    answer = set()
    x, y = 0, 0
    
    for dir in dirs:
        i = d[dir]
        
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < -5 or ny < -5 or nx > 5 or ny > 5:
            continue
            
        answer.add((nx, ny, x, y))
        answer.add((x, y, nx, ny))
        
        x, y = nx, ny
        
    return len(answer) // 2