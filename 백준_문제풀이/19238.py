from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 현 위치에서 다른 지점까지의 거리를 구한다.
def find_search(x, y):
    distance = [[-1] * n for _ in range(n)]
    distance[x][y] = 0

    visit = [[False] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == False and graph[nx][ny] != 1:
                    q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
                    visit[nx][ny] = True
    return distance
                    

n, m, l = map(int, input().split())
graph  = [list(map(int, input().split())) for _ in range(n)]
# -1을 하여 사용하기 쉽게 만들어준다.
s_x, s_y = map(int, input().split())
s_x -= 1
s_y -= 1

# for else문을 쓰려다가, 알아보기 힘들것같아 
# flag을 만들어줘서, 중간에 나오면 -1을 출력해주기 위한 변수
flag = True
move = []
for _ in range(m):
    sx, sy, ex, ey = map(int, input().split())
    sx -= 1
    sy -= 1
    ex -= 1
    ey -= 1
    move.append((sx,sy, ex, ey))
# move라는 고객의 위치와 도착위치를 알려주는 배열을 만들어준다.

for case in range(m):
    candidate = []
    # 현 위치에서 걸리는 거리 검색
    distance = find_search(s_x, s_y)
    
    for i in range(len(move)):
        temp = move[i]
        dist = distance[temp[0]][temp[1]]
        candidate.append((dist, temp[0], temp[1], temp[2], temp[3]))
        
    # 거리순, 행, 열 순으로 정렬
    candidate.sort(key = lambda x : (x[0], x[1], x[2]))

    # 만족하는 손님 선택
    elect = candidate.pop(0)
    elect = list(elect)

    # 만족하는 손님과의 거리가 -1이면 못간다는것이므로 종료
    if elect[0] == -1:
        flag = False
        break

    # 손님한테 가는 거리 추가, 이동하는 도중 0이하면 실패
    l = l - elect.pop(0)
    if l <= 0:
        flag = False
        break

    # 손님시작에서 종료까지 거리 추가, 종료지점에서 0미만이면 실패, 0이상이면 성공
    d = find_search(elect[0], elect[1])

    # 종료지점으로 이동하는데 거리가 -1이면 못간다는것이므로 종료
    if s_x == elect[0] and s_y == elect[1]:
        if d == -1:
            flag = False
            break

	# 손님을 태우고 목적지까지 이동중 연료를 사용하니 빼주고, 만약 0보다 작으면 실패
    # 하지만 목적지에 도착했을때 0이어도 성공이기 때문에 0 미만으로 해준다.
    l = l - d[elect[2]][elect[3]]
    if l < 0:
        flag = False
        break
        
    # 도착했으니 2배 충전
    l = l + (d[elect[2]][elect[3]] * 2)
    
    # 해치운 손님 제거
    move.remove(tuple(elect))

    # 손님의 종착지로 다시 시작
    s_x, s_y = elect[2], elect[3]

# 정상적인 종료면 남은 연료 출력, 중간에 실패하면 -1 출력
if flag:
    print(l)
else:
    print(-1)