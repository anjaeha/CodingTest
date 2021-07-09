import sys
input = sys.stdin.readline

n = int(input())
enter = {}
out = []
cnt = 0

for i in range(n):
    car = input().strip()
    enter[car] = i

for i in range(n):
    car = input().strip()
    out.append(car)

for i in range(n - 1):
    for j in range(i + 1, n):
        if enter[out[i]] > enter[out[j]]:
            cnt += 1
            break

print(cnt)