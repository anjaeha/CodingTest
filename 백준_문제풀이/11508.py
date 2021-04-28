import sys
input = sys.stdin.readline

n = int(input())

cost = []
for i in range(n):
    cost.append(int(input()))

cost.sort(reverse=True)

if n < 3:
    print(sum(cost))
else:
    for i in range(n):
        if (i+1) % 3 == 0:
            cost[i] = 0
    print(sum(cost))