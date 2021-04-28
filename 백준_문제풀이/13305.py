import sys
input = sys.stdin.readline

n = int(input())

d = list(map(int, input().split()))
c = list(map(int, input().split()))

answer = 0
cost = 1000000001
for i in range(n-1):
    if c[i] < cost:
        cost = c[i]
    answer += cost * d[i]

print(answer)