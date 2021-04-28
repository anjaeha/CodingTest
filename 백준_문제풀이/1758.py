import sys
input = sys.stdin.readline

n = int(input())
m = []

for i in range(n):
    m.append(int(input()))

m.sort(reverse=True)
for i in range(n):
    m[i] = m[i] - i
    if m[i] < 0:
        m[i] = 0

print(m)