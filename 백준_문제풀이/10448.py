import sys
input = sys.stdin.readline

t = [n * (n+1) // 2 for n in range(1, 46)]
e = [0] * 1001

for i in t:
    for j in t:
        for k in t:
            if i + j + k <= 1000:
                e[i+j+k] = 1

n = int(input())

for i in range(n):
    k = int(input())
    if e[k] == 1:
        print(1)
    else:
        print(0)