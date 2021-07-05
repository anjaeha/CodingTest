import sys
input = sys.stdin.readline

t = int(input())

for case in range(t):
    s = input().strip()

    left = []
    right = []

    for i in s:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    print(''.join(left) + ''.join(reversed(right)))