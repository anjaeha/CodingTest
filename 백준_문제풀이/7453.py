import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
a, b, c, d = [], [], [], []

for _ in range(n):
    x, y, z, k = map(int, input().split())
    a.append(x)
    b.append(y)
    c.append(z)
    d.append(k)

first = []
second = []

for i in range(n):
    for j in range(n):
        first.append(a[i] + b[j])
        second.append(c[i] + d[j])

counter = Counter(second)
answer = 0
for num in first:
    answer += counter[-num]

print(answer)