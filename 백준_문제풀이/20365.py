import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

r = 'R'
b = 'B'
start = s[0]
count = [1] * 3

for i in s:
    if i != start:
        count[0] += 1
        start = i

    if i == 'R':
        if b == 'B':
            count[1] += 1
            b = 'R'
        r = 'R'
    else:
        if r == 'R':
            count[2] += 1
            r = 'B'
        b = 'B'

print(min(count))