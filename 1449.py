n, l = map(int, input().split())
t = list(map(int, input().split()))
t.sort()

s = t[0]
e = t[0] + l
cnt = 1

for i in range(n):
    if s <= t[i] < e:
        continue
    else:
        s = t[i]
        e = t[i] + l
        cnt += 1

print(cnt)
