n, new, p = map(int, input().split())

if n:
    score = list(map(int, input().split()))
    score.append(new)
    score.sort(reverse=True)

    idx = score.index(new) + 1

    if idx > p:
        print(-1)
    else:
        if n == p and new == score[-1]:
            print(-1)
        else:
            print(idx)

else:
    print(1)