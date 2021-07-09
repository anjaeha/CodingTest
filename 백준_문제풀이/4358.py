import sys
input = sys.stdin.readline

wood = {}
n = 0
while 1:
    x = input().strip()
    if not x:
        break
    if x in wood:
        wood[x] += 1
    else:
        wood[x] = 1
    n += 1

lst = sorted(list(wood.keys()))
for i in lst:
    print('%s %.4f' %(i, wood[i] * 100 / n))