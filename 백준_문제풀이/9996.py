import sys, re
input = sys.stdin.readline

n = int(input())
s = input().strip()
s = s.replace('*', '.*')
file = [input().strip() for _ in range(n)]
answer = []


for f in file:
    p = re.compile(s)
    m = p.match(f)
    if m:
        answer.append('DA')
    else:
        answer.append('NE')

for i in answer:
    print(i)