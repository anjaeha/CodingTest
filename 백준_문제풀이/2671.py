import sys, re
input = sys.stdin.readline

n = input().strip()
p = re.compile('(100+1+|01)+')

m = p.fullmatch(n)
if m:
    print('SUBMARINE')
else:
    print('NOISE')
