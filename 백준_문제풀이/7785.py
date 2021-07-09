import sys
input = sys.stdin.readline

n = int(input())
member = {}

for i in range(n):
    name, act = input().strip().split()
    if act == 'enter':
        member[name] = 'enter'
    else:
        del member[name]

answer = sorted(member.keys(), reverse=True)
for i in answer:
    print(i)