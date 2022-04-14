n, k = map(int, input().split())
belt = list(map(int, input().split()))

robot = [False] * (2 * n)

def rotate():
    belt.insert(0, belt.pop())
    robot.insert(0, robot.pop())

def robot_move():
    for idx in range(n, -1, -1):
        if robot[idx]:
            if idx == n - 1 or idx == n:
                robot[idx] = False
            else:
                if belt[idx + 1] > 0 and not robot[idx + 1]:
                    belt[idx + 1] -= 1
                    robot[idx + 1] = True
                    robot[idx] = False

def robot_raise():
    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

def check():
    cnt = 0
    for i in range(2 * n):
        if belt[i] == 0:
            cnt += 1
    if cnt >= k:
        return True
    return False

result = 1
while 1:
    rotate()
    robot_move()
    robot_raise()
    if check():
        break
    result += 1

print(result)