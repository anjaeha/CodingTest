n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0] * n
# 올리는 위치는 0번, 내리는 위치 n -1, 

# 컨베이어 벨트 돌아감
def move():
    # 2n - 1이 0번으로 이동
    belt.insert(0, belt.pop())
    robot.pop()
    robot.insert(0, 0)

# 로봇 움직임
def robot_move():
    for i in range(n -2, -1, -1):
        if robot[i] == 1 and robot[i + 1] == 0:
            if belt[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1

# 0번에서 로봇 올림
def put_robot():
    if belt[0] >= 1:
        belt[0] -= 1
        robot[0] = 1

# 0이 K개 있는지 확인
def check():
    cnt = 0
    for i in range(2 * n):
        if belt[i] == 0:
            cnt += 1
    if cnt >= k:
        return False
    return True

# n - 1에 로봇이 있으면 떨어뜨림
def fall_robot():
    if robot[n - 1] == 1:
        robot[n - 1] = 0

result =  0
while 1:
    result += 1
    move() # 1번 조건
    fall_robot() # 로봇은 즉시 떨어지기에 확인필요
    robot_move() # 2번 조건
    fall_robot() # 로봇은 즉시 떨어지기에 확인필요
    put_robot() # 3번 조건
    if check(): # 4번 조건
        pass
    else:
        break

print(result)