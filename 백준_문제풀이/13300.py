import sys
from math import ceil
input = sys.stdin.readline

n, k = map(int, input().split())

stduent = [[0] * 2 for _ in range(6)]

for i in range(n):
    s, y = map(int, input().split())
    stduent[y-1][s] += 1

room = 0
for i in range(6):
    for j in range(2):
        room += ceil(stduent[i][j] / k)

print(room)