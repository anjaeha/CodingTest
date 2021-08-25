def makeSum(arr):
    result = 0
    idx = 0
    for i in range(k):
        temp = 0
        while 1:
            temp += arr[idx]
            idx = (idx + 1) % n
            if temp + arr[idx] > m:
                break
        result += temp
    return result

import sys
input = sys.stdin.readline
from itertools import permutations

n, m, k = map(int, input().split())
s = list(map(int, input().split()))
MIN = sys.maxsize
array = list(permutations(s, n))

for i in array:
    temp = makeSum(i)
    MIN = min(MIN, temp)

print(MIN)