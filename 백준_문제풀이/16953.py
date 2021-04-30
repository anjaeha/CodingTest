import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 1


while a != b:
    if b % 2 == 0:
        cnt += 1
        b = b // 2
    else:
        b = str(b)
        b = list(b)
        if b[-1] != '1':
            cnt = -1
            break
        b.pop()
        b = ''.join(b)
        if b == '':
            cnt = -1
            break
        b = int(b)
        cnt += 1

print(cnt)