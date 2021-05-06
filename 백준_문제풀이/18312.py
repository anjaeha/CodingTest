import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0

for i in range(n+1):
    if i < 10:
        i = '0' + str(i)
    for j in range(60):
        if j < 10:
            j = '0' + str(j)
        for q in range(60):
            if q < 10:
                q = '0' + str(q)
            if str(k) in str(i) + str(j) + str(q):
                cnt += 1


print(cnt)