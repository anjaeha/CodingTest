import sys
input = sys.stdin.readline

n = int(input())

info = []
p = 0

for i in range(n):
    x = list(map(int, input().split()))
    info.append(x)
    p += x[1]

info.sort()

mid = p // 2
if p % 2 == 1:
    mid += 1

cnt = 0
for l, p in info:
    cnt += p

    if cnt >= mid:
        print(l)
        break