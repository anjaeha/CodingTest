import sys
input = sys.stdin.readline

t = int(input())

s = dict()

for i in range(t):
    e = input().strip().split('.')[1]

    if e not in s:
        s[e] = 1
    else:
        s[e] += 1

s = sorted(s.items(), key = lambda x : x[0])

for i in range(len(s)):
    print(s[i][0], s[i][1])