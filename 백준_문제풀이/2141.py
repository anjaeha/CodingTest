import sys
input = sys.stdin.readline

n = int(input())

info = []
people = 0

for i in range(n):
    x = list(map(int,input().split()))
    info.append(x)
    people+=x[1]

info = sorted(info)

mid = people // 2
if people % 2 == 1:
    mid += 1


cnt = 0

for i, l in info:
    cnt += l

    if cnt >= mid:
        print(i)
        break


print(mid)