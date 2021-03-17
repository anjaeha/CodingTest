n = int(input())

p = list(map(int, input().split()))

p.sort()

cnt = 0
s = 0

for i in range(n):
    cnt += p[i]
    s += cnt

print(s)