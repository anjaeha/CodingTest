import sys
input = sys.stdin.readline

n = int(input())
room = []

for i in range(n):
    room.append(list(map(int, input().split())))

room.sort()
count = []

for i in range(n):
    if i == 0:
        count.append(room[i][1])
        continue

    chk = 1

    for j in range(len(count)):
        if room[i][0] >= count[j]:
            chk = 0
            count[j] = room[i][1]
            break
    
    if chk == 1:
        count.append(room[i][1])

print(len(count))