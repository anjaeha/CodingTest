import sys
input = sys.stdin.readline

i = 1
while 1:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    result = 0
    result += v // p * l

    if v % p > l:
        result += l
    else:
        result += v % p
    print("Case %d: %d" %(i, result))
    i += 1