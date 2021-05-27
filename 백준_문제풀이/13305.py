import sys
input = sys.stdin.readline

n = int(input())
load = list(map(int, input().split()))
cost = list(map(int, input().split()))

money = 0
idx = 0
for i in range(n-1):
    if cost[idx] > cost[i]:
        idx = i
    money += cost[idx] * load[i]

print(money)