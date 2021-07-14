import sys
input = sys.stdin.readline

t = int(input())

for case in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))

    impo = [0] * n
    impo[m] = 1
    cnt = 1
    while 1:
        if s[0] == max(s):
            if impo[0] == 1:
                print(cnt)
                break
            s.pop(0)
            impo.pop(0)
            cnt += 1
        else:
            s.append(s.pop(0))
            impo.append(impo.pop(0))