def solution(dirs):
    answer = set()
    x, y = 0, 0
    
    for dire in dirs:
        nx, ny = x, y
        if dire == 'U':
            nx -= 1
        elif dire == 'D':
            nx += 1
        elif dire == 'L':
            ny -= 1
        elif dire == 'R':
            ny += 1
        
        if nx < -5 or ny < -5 or nx > 5 or ny > 5:
            continue
        else:
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x, y = nx, ny
    
    return len(list(answer)) // 2