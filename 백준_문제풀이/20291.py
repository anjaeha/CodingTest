import sys
input = sys.stdin.readline

n = int(input())

file = dict()

for i in range(n):
    ext = (input().split('.'))[1]
    if not ext in file:
        file[ext] = 1
    else:
        file[ext] += 1

file_sort = sorted(file.items())

for key, value in file_sort:
    print(key.rstrip(), value)