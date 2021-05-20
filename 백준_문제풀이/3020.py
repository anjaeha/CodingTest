import sys
input = sys.stdin.readline

n, h = map(int, input().split())

top = [0] * (h+1)
bot = [0] * (h+1)

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        bot[num] += 1
    else:
        top[h - num + 1] += 1

for i in range(h-1, 0, -1):
    bot[i] += bot[i+1]

for i in range(1, h+1):
    top[i] += top[i-1]

total = [0] * (h+1)

for i in range(1, h+1):
    total[i] = bot[i] + top[i]

total = total[1:]
MIN = min(total)

cnt = 0
for i in total:
    if i == MIN:
        cnt += 1

print(MIN, cnt)
print(top)