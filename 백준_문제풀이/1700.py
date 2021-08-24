import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))

tab = []
result = 0
for i in range(k):
    if s[i] in tab:
        continue

    if len(tab) < n:
        tab.append(s[i])
        continue

    result += 1
    out = 0
    outidx = 0
    for j in range(n):
        try:
            idx = s[i+1:].index(tab[j])
            if idx > outidx:
                out = j
                outidx = idx
        except:
            out = j
            break

    tab[out] = s[i]

print(result)