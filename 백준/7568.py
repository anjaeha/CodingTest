
N = int(input())

a = []

for i in range(N):
    a.append(input().split())

seq = []

for i in range(len(a)):
    cnt = 1
    for j in range(len(a)):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            cnt += 1

    seq.append(cnt)

print(*seq)