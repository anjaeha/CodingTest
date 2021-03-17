M = int(input())
N = int(input())

arr = []

for i in range(2, N+1):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
    if cnt == 0 and i >= M and i <=N:
        arr.append(i)


if not arr:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))