import sys
input = sys.stdin.readline

s = []
for i in range(5):
    s.append(list(input().strip()))

for i in range(max([len(e) for e in s])):
    for j in range(5):
        if i < len(s[j]):
            print(s[j][i], end = '')