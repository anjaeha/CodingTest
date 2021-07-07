import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0
for i in a:
    cnt += 1
    temp = i - b
    
    if temp > 0:
        if temp % c == 0:
            cnt += temp // c
        else:
            cnt += temp // c + 1

print(cnt)