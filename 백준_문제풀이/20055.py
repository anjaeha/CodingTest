from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
answer = 0
convey = deque(list(map(int, input().split())))
robot = deque([0] * n)

while convey.count(0) < k:
    convey.rotate(1)
    robot.rotate(1)

    robot[n - 1] = 0
    if sum(robot) != 0:
        for idx in range(n-2, -1, -1):
            if robot[idx] == 1 and robot[idx + 1] == 0 and convey[idx + 1] != 0:
                robot[idx] = 0
                robot[idx + 1] = 1
                convey[idx + 1] -= 1

        robot[n - 1] = 0

    if robot[0] == 0 and convey[0] != 0:
        robot[0] = 1
        convey[0] -= 1

    answer += 1

print(answer)