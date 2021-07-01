import sys
input = sys.stdin.readline


t = int(input())

for case in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    impo = [0 for _ in range(n)]
    impo[m] = 1
    cnt = 0

    while 1:
        if s[0] == max(s):
            cnt += 1
            if impo[0] == 1:
                print(cnt)
                break
            else:
                s.pop(0)
                impo.pop(0)
        else:
            s.append(s.pop(0))
            impo.append(impo.pop(0))