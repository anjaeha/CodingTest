import sys
input = sys.stdin.readline
from math import factorial

t = int(input())

for case in range(t):
    w, e = map(int, input().split())
    
    result = factorial(e) // factorial(w) // factorial(e-w)

    print(result)