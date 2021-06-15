import sys
input = sys.stdin.readline

n = int(input())
s = [set() for _ in range(101)]

for _ in range(n):
    number = input().strip()

    for i in range(1, len(number) + 1):
        s[i].add(number[-i:])

for i in range(1, 101):
    if len(s[i]) == n:
        print(i)
        break