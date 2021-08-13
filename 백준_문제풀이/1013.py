import sys, re
input = sys.stdin.readline

n = int(input().strip())

result = []
for i in range(n):
    sign = input().strip() 
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(sign)
    if m:
        result.append('YES')
    else:
        result.append('NO')

for i in result:
    print(i)
