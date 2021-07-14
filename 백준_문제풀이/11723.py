import sys
input = sys.stdin.readline

n = int(input())

s = set()
for _ in range(n):
    tmp = input().strip().split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = set(i for i in range(1, 21))
        else:
            s = set()

        continue

    word, num = tmp[0], int(tmp[1])
    if word == 'add':
        s.add(num)
    elif word == 'remove':
        s.discard(num)
    elif word == 'check':
        sys.stdout.write('1\n' if num in s else '0\n')
    elif word == 'toggle':
        if num in s:
            s.discard(num)            
        else:
            s.add(num)