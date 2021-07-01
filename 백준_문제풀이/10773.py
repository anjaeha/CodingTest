import sys
input = sys.stdin.readline

k = int(input())

s = []
for i in range(k):
    x = int(input())

    if x != 0:
        s.append(x)
    else:
        if s == []:
            continue
        else:
            s.pop()

print(sum(s))