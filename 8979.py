N, K = map(int, input().split())
arr = []

for case in range(N):
    arr.append(list(map(int, input().split())))


arr.sort(key = lambda x: (-x[1], -x[2], -x[3]))

for i in range(N):
    if arr[i][0] == K:
        index = i


for i in range(N):
    if arr[index][1:] == arr[i][1:]:
        print(i+1)
        break


#