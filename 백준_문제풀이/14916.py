import sys
input = sys.stdin.readline

n = int(input())

cnt = 0

while n > 0:
    if n % 5 == 0:
        cnt += n // 5
        n = n % 5
    else:
        cnt += 1
        n -= 2

if n < 0:
    print(-1)
else:
    print(cnt)