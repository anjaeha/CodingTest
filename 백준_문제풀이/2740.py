a = []
b = []

n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
for i in range(m):
    b.append(list(map(int, input().split())))

c = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for q in range(m):
            c[i][j] += a[i][q] * b[q][j]

for i in c:
    for j in i:
        print(j, end = ' ')
    print()
