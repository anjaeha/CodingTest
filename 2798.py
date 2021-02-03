N, M = map(int, input().split())

num = list(map(int, input().split()))

mi = []

for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if num[i] + num[j] + num[k] <= M:
                mi.append(num[i] + num[j] + num[k])

print(max(mi))