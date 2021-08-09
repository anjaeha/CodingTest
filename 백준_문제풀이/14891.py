import sys
input = sys.stdin.readline

one = list(map(int, input().strip()))
two = list(map(int, input().strip()))
three = list(map(int, input().strip()))
four = list(map(int, input().strip()))
gear = [[], one, two, three, four]

k = int(input())

lotate = [list(map(int, input().split())) for _ in range(k)]

def up(arr):
    arr.insert(0, arr.pop())

def down(arr):
    arr.append(arr.pop(0))


def move(x, num):
    if not check[x]:
        check[x] = True
        x_left = gear[x][6]
        x_right = gear[x][2]

        if num == 1:
            up(gear[x])
        elif num == -1:
            down(gear[x])

        if x != 1 and x_left != gear[x-1][2]:
            move(x-1, -num)
        if x != 4 and x_right != gear[x+1][6]:
            move(x+1, -num)

for i in range(k):
    x, y = lotate[i][0], lotate[i][1]
    check = [False] * 5

    move(x, y)


answer = 0
for i in range(1, 5):
    answer += gear[i][0] * (2 ** (i-1))

print(answer)