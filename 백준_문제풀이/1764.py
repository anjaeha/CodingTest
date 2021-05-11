import sys
input = sys.stdin.readline

n, m = map(int, input().split())

h = set()
s = set()

for i in range(n):
    h.add(input().strip())

for i in range(m):
    s.add(input().strip())


answer = sorted(list(h & s))

print(len(answer))
for i in answer:
    print(i)