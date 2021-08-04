import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
number = list(map(int, input().split()))

p = []
s = []

for i in range(m):
    if number[i] in p:
        k = p.index(number[i])
        s[k] += 1
    else:
        if len(p) != n:
            p.append(number[i])
            s.append(0)
        else:
            temp = min(s)
            temp_index = s.index(temp)
            s.pop(temp_index)
            p.pop(temp_index)
            s.append(0)
            p.append(number[i])

p.sort()
print(*p)