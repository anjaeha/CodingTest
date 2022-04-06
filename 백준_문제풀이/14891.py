gears = [list(input()) for _ in range(4)]
m = int(input())
dir = [list(map(int, input().split())) for _ in range(m)]

def rotate(arr, d):
    if d == 1: # 시계방향으로 회전
        arr.insert(0, arr.pop())
    elif d == -1:
        arr.append(arr.pop(0))

def move(pos, d):
    visit[pos] = True
    left, right = gears[pos][6], gears[pos][2]
    rotate(gears[pos], d)

    if pos == 0:
        if right != gears[1][6] and not visit[1]:
            move(1, -d)
    elif pos == 3:
        if left != gears[2][2] and not visit[2]:
            move(2, -d)
    else:
        if right != gears[pos + 1][6] and not visit[pos + 1]:
            move(pos + 1, -d)
        if left != gears[pos - 1][2] and not visit[pos - 1]:
            move(pos - 1, -d)

for idx in range(m):
    pos, d = dir[idx]
    pos -= 1
    visit = [False] * 4
    move(pos, d)

result = 0
for i in range(4):
    if int(gears[i][0]):
        result += 2 ** i

print(result)