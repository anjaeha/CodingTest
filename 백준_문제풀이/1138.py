import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
a = [0 for _ in range(n)]

for i in range(n+1):
    cnt = 0
    k = s[i-1]

    for j in range(n):
        if cnt == k and a[j] == 0:
            a[j] = i
            break
        elif a[j] == 0:
            cnt += 1

print(*a)