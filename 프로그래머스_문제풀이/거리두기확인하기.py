# 4방향을 확인하고 막혀있으면 방향의 +-1을 확인하지 않아도됨.
# 안막혀있으면 - 거기서 3방향 확인, 거기에 사람이 있으면 실패
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(p, x, y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx <= 4 and 0 <= ny <= 4:
            if p[nx][ny] == 'P': # 사람이 있으면 실패
                return False
            elif p[nx][ny] == 'O': # 빈자리면 한번 더 확인
                for dd in range(4):
                    nnx = nx + dx[dd]
                    nny = ny + dy[dd]
                    
                    if 0 <= nnx <= 4 and 0 <= nny <= 4:
                        if nnx == x and nny == y:
                            continue
                        if p[nnx][nny] == 'P':
                            return False
            elif p[nx][ny] == 'X': # 막혀있으면 다른방향 확인해야함
                continue
    return True

def solution(places):
    answer = []
    for place in places:
        flag = True
        for x in range(5):
            for y in range(5):
                if flag and place[x][y] == 'P':
                    result = check(place, x, y)
                    if not result:
                        flag = False
        
        if flag:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer