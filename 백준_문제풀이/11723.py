import sys
input = sys.stdin.readline

s = [0] * 21
n = int(input())

for _ in range(n):
    tmp = input().strip().split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = [1] * 21
        else:
            s = [0] * 21
        continue

    word = tmp[0]
    num = int(tmp[1])

    if word == 'add':
        s[num] = 1
    elif word == 'remove':
        s[num] = 0
    elif word == 'check':
        if s[num] == 1:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif word == 'toggle':
        s[num] = abs(s[num] - 1)