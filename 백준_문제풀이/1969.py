import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())

dna = [list(input().strip()) for _ in range(n)]

result = ''
hd = 0

for i in range(m):
    cnt = [0, 0, 0, 0]
    for j in range(n):
        if dna[j][i] == 'A':
            cnt[0] += 1
        elif dna[j][i] == 'C':
            cnt[1] += 1
        elif dna[j][i] == 'G':
            cnt[2] += 1
        elif dna[j][i] == 'T':
            cnt[3] += 1

    Max = max(cnt)

    idx = cnt.index(Max)

    if idx == 0:
        result += 'A'
    elif idx == 1:
        result += 'C'
    elif idx == 2:
        result += 'G'
    elif idx == 3:
        result += 'T'

    hd += n - Max

print(result)
print(hd)