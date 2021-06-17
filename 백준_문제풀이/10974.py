import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
s = [i for i in range(1, n+1)]
answer = permutations(s, n)

for i in answer:
    print(*i)