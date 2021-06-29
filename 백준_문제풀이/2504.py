import sys
input = sys.stdin.readline

s = input().strip()

small = []
large = []

cnt = 1
flag = True
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        small.append(i)
        cnt *= 2
    elif s[i] == '[':
        large.append(i)
        cnt *= 3
    elif s[i] == ')':
        if small:
            if s[i-1] == '(':
                ans += cnt
            small.pop()
            cnt //= 2
        else:
            flag = False
            break
    elif s[i] == ']':
        if large:
            if s[i - 1] == '[':
                ans += cnt
            large.pop()
            cnt //= 3
        else:
            flag = False
            break

print(ans if not small and not large and flag else 0)