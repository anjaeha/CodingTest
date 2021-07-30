import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))

command = []
for _ in range(m):
    command.append(list(map(int, input().split())))

for i in range(m):
    if command[i][0] == 1:
        data[command[i][1] - 1] = command[i][2]
    elif command[i][0] == 2:
        for j in range(command[i][1] - 1, command[i][2]):
            data[j] = abs(data[j] - 1)
    elif command[i][0] == 3:
        for j in range(command[i][1] - 1, command[i][2]):
            data[j] = 0
    elif command[i][0] == 4:
        for j in range(command[i][1] - 1, command[i][2]):
            data[j] = 1

print(*data)