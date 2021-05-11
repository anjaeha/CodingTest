import sys
input = sys.stdin.readline

tmp = ''
ans = ''
ck = False

s = input().strip()

for i in s:
    if i == ' ':
        if not ck:
            ans += tmp[::-1] + i
            tmp = ''
        else:
            ans += i
    elif i == '<':
        ck = True
        ans += tmp[::-1] + i
        tmp = ''
    elif i == '>':
        ck = False
        ans += i
    else:
        if ck:
            ans += i
        else:
            tmp += i

ans += tmp[::-1]
print(ans)
    