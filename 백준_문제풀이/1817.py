import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n == 0:
    print(0)
    exit()
    
book = list(map(int, input().split()))[::-1]
w = m
cnt = 1
for i in range(n):
    if w - book[i] < 0:
        cnt += 1
        w = m
    w -= book[i]

print(cnt)
