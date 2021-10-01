gear = [[]] + [list(input()) for _ in range(4)]

k = int(input())
rotate = [list(map(int, input().split())) for _ in range(k)]

def clock_rotate(arr): # 시계방향으로
    # 시계방향은, 7번이 1번으로 가면 됨.
    arr.insert(0, arr.pop())

def anticlock_rotate(arr): # 반시계방향으로
    # 반시계방향은, 1번이 7번으로 가면 됨.
    arr.append(arr.pop(0))

def move(idx, dir):
    global gear
    right = gear[idx][6]
    left = gear[idx][2]
    if dir == 1 and visit[idx] == False:
        clock_rotate(gear[idx])
        visit[idx] = True
    elif dir == -1 and visit[idx] == False:
        anticlock_rotate(gear[idx])
        visit[idx] = True
    else:
        return

    if idx == 1:
        if visit[idx + 1] == False:
            if left != gear[idx + 1][6]:
                move(idx + 1, -dir)
    elif idx == 2 or idx == 3:
        if visit[idx + 1] == False:
            if left != gear[idx + 1][6]:
                move(idx + 1, -dir)
        if visit[idx - 1] == False:
            if right != gear[idx - 1][2]:
                move(idx - 1, -dir)
    elif idx == 4:
        if visit[idx - 1] == False:
            if right != gear[idx - 1][2]:
                move(idx - 1, -dir)
    
    return

for case in range(k):
    target, dir = rotate[case]
    visit = [False] * 5
    move(target, dir)
    

result = 0
for i in range(1, 5):
    if gear[i][0] == '1':
        result = result + (2 ** (i - 1))

print(result)