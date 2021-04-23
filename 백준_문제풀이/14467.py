import sys
input = sys.stdin.readline

n = int(input())
s = [-1] * 11
cnt = 0

for i in range(n):
    cow, pos = map(int, input().split())

    if s[cow] == -1:
        s[cow] = pos
    else:
        if s[cow] != pos:
            s[cow] = pos
            cnt += 1

print(cnt)