while True:
    N = int(input())
    if N == 0:
        break
    if N == 1:
        print(1)
        continue

    arr = []
    num = set(i for i in range(2, 2*N+1))
    for i in range(2, 2*N+1):
        if i in num:
            num -= set(range(i*2, 2*N+1, i))

    cnt = 0
    for k in num:
        if k > N and k <= 2*N:
            cnt += 1

    print(cnt)