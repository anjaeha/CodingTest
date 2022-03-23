# 1번에서 올리고, N번에서 내림
# 로봇을 올리거나 움직이면 내구도 -1
# 벨트 회전 -> 로봇 이동 -> 로봇 올림 -> 내구도 검사

def belt_move():
    down_belt.insert(0, up_belt.pop())
    up_belt.insert(0, down_belt.pop())
    robot.pop()
    robot.insert(0, False)

def robot_move():
    for idx in range(n - 1, -1, -1):
        if robot[idx]:
            if idx == n - 1:
                robot[idx] = False
            else:
                if not robot[idx + 1] and up_belt[idx + 1] > 0:
                    robot[idx + 1] = True
                    robot[idx] = False
                    up_belt[idx + 1] -= 1

def raise_robot():
    if up_belt[0] > 0:
        robot[0] = True
        up_belt[0] -= 1

def check():
    cnt = 0
    for i in range(n):
        if up_belt[i] == 0:
            cnt += 1
        if down_belt[i] == 0:
            cnt += 1
    if cnt >= k:
        return True
    return False

n, k = map(int, input().split())
belt = list(map(int, input().split()))
up_belt = belt[:n]
down_belt = belt[n:]
robot = [False] * n

count = 1
while 1:
    belt_move()
    robot_move()
    raise_robot()
    if check():
        break
    count += 1

print(count)