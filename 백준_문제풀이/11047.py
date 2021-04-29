import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))


cnt = 0
for i in range(n-1, -1, -1):
    cnt =  cnt + k // coin[i]
    k = k % coin[i]

print(cnt)