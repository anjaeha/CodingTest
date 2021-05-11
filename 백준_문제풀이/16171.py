import sys
input = sys.stdin.readline

s = input().strip()
k = input().strip()
s_alpha = ''
for i in s:
    if i.isalpha():
        s_alpha += i

if k in s_alpha:
    print(1)
else:
    print(0)