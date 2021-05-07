import sys
input = sys.stdin.readline


for case in range(int(input())):
    s = input()
    li = [0] * 26

    for i in s:
        if i.isalpha():
            li[ord(i) - ord('a')] += 1
    t = max(li)

    print(chr(ord('a') + li.index(t)) if li.count(t) < 2 else '?')