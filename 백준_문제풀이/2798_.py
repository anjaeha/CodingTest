import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
card = sorted(list(map(int, input().split())))

permute = permutations(card, 3)
permute_sum = []

for i in permute:
    if sum(i) <= m:
        permute_sum.append(sum(i))

print(max(permute_sum))