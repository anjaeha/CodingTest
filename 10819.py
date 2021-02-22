from itertools import permutations

n = int(input())

arr = list(map(int, input().split()))

p = list(permutations(arr, n))
r = 0

for i in p:
    s = 0
    li = list(i)
    for j in range(1, n):
        s += abs(li[j] - li[j-1])
    r = max(r,s)

print(r)