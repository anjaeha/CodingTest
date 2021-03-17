T = int(input())

t = []
sum = []

for case in range(T):
    t.append(list(map(int, input().split())))


k = 2

for i in range(1, T):
    for j in range(k):
        if j == 0: # 맨 왼쪽 숫자면
            t[i][j] = t[i][j] + t[i-1][j]
        elif i == j: # 맨 오른쪽 숫자면
            t[i][j] = t[i][j] + t[i-1][j-1]
        else: # i-1에서 왼쪽이 큰지 오른쪽이 큰지 비교해서 더하기
            t[i][j] = max(t[i-1][j], t[i-1][j-1]) + t[i][j]

    k += 1

print(max(t[T-1]))