import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pockmon_1 = {}
pockmon_2 = {}
number = 1

for _ in range(n):
    name = input().strip()
    pockmon_1[name] = number
    pockmon_2[number] = name
    number += 1


answer = []
for _ in range(m):
    x = input().strip()
    if x.isdigit():
        answer.append(pockmon_2[int(x)])
    else:
        answer.append(pockmon_1[x])

for i in answer:
    print(i)