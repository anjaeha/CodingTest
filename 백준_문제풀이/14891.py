# 시계방향 1, 반시계방향 -1
def clock(arr, d):
    if d == 0:
        return
    elif d == 1: # 시계 방향
        arr.insert(0, arr.pop())
        return
    elif d == -1: #반시계 방향
        arr.append(arr.pop(0))
        return

gear = [list(input()) for _ in range(4)]
k = int(input())
# 2번이 오른쪽, 6번이 왼쪽

for i in range(k):
    target, dir = map(int, input().split())
    target -= 1

    move = [0] * 4
    move[target] = dir
    right, left = dir, dir

    for j in range(target + 1, 4): # 오른쪽 톱니바퀴 확인
        if gear[j - 1][2] == gear[j][6]:
            break
        else:
            move[j] = -right
            right = -right

    for j in range(target - 1, -1, -1): # 왼쪽 톱니바퀴 확인
        if gear[j + 1][6] == gear[j][2]:
            break
        else:
            move[j] = -left
            left = -left

    for j in range(4):
        clock(gear[j], move[j])


# N극이면 0, S극이면 1
result = 0
for i in range(4):
    result += int(gear[i][0]) * (2 ** i)
print(result)