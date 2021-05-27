import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)
cnt = 0

for i in range(n):
    if k >= coin[i]:
        cnt += k // coin[i]
        k = k % coin[i]
print(cnt)