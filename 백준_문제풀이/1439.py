import sys
input = sys.stdin.readline

s = list(map(int, input().strip()))

cnt = 1
li = len(s)
cnt_0 = 0
cnt_1 = 0

num = -1
for i in range(li):
    if num != s[i]:
        if s[i] == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1
        num = s[i]
print(min(cnt_0, cnt_1))