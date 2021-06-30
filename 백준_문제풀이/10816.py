from collections import Counter

n = int(input())
n_list = sorted(list(map(int, input().split())))

m = int(input())
m_list = list(map(int, input().split()))

n_list = Counter(n_list)

for i in m_list:
    print(n_list[i], end = ' ')



"""
import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
n_arr = sorted(list(map(int, input().split())))

m = int(input())
m_arr = list(map(int, input().split()))

hashmap = {}
for i in n_arr:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1


for i in m_arr:
    if i in hashmap:
        print(hashmap[i], end = ' ')
    else:
        print(0, end = ' ')
"""