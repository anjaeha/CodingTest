import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

member = [i for i in range(n)]
cases = list(combinations(member, n // 2))
value = 101

for case_a in cases:
    A = 0
    B = 0

    for x in case_a:
        for y in case_a:
            A += s[x][y]
    
    case_b = [i for i in range(n) if i not in case_a]
    for x in case_b:
        for y in case_b:
            B += s[x][y]

    value = min(value, abs(A-B))

print(value)