n = int(input())
l = list(map(int, input().split()))

def f(l):
    if len(l) == 3:
        return l[0] * l[2]

    ret = 0
    for i in range(1, len(l) - 1):
        r = l[i+1] * l[i-1] + f(l[:i] + l[i+1:])
        ret = max(r, ret)

    return ret

print(f(l))