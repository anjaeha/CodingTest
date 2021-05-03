import sys
input = sys.stdin.readline

n = int(input())
s = sorted(list(map(int, input().split())), reverse=True)

m = int(input())
box = sorted(list(map(int, input().split())), reverse=True)


if s[0] < box[0]:
    print(-1)
    exit()

cnt = 0

while box:
    cnt += 1

    for i in s:
        for j in range(len(box)):
            if i >= box[j]:
                i = i - box[j]
                del box[j]
                break

print(box)