N = int(input())

t = []
r, c = 0, 0
cnt = 0

for case in range(N):
    t.append(list(input()))

for i in range(N):
    cnt = 0
    for j in range(N):
        if t[i][j] == '.':
            cnt += 1
        else:
            cnt = 0

        if cnt == 2:
            r += 1

for i in range(N):
    cnt = 0
    for j in range(N):
        if t[j][i] == '.':
            cnt += 1
        else:
            cnt = 0

        if cnt == 2:
            c += 1

print(r,c)