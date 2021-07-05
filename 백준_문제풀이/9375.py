import sys
input = sys.stdin.readline
from itertools import combinations

t = int(input())

for case in range(t):
    n = int(input())
    if n == 0:
        print(0)
        continue

    answer = {}
    for i in range(n):
        wear, category = input().split()
        if category in answer:
            answer[category] += 1
        else:
            answer[category] = 1

    s = list(answer.values())

    cnt = 1
    
    for i in s:
        cnt *= (i+1)

    print(cnt - 1)