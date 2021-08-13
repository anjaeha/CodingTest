import sys
input = sys.stdin.readline

n = list(input().strip())

cnt = 0
for i in range(len(n)):
    if n[i].isupper():
        while ((i+cnt) % 4 != 0):
            cnt += 1
print(cnt)