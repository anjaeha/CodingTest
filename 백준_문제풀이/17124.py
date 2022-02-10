import sys
input = sys.stdin.readline
from bisect import bisect_left

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    n_arr = list(map(int, input().split()))
    m_arr = sorted(list(map(int, input().split())))
    c = []

    for i in range(n):
        left = bisect_left(m_arr, n_arr[i])

        if left >= m:
            c.append(m_arr[-1])
            continue

        temp_l = abs(m_arr[left - 1] - n_arr[i])
        temp_r = abs(m_arr[left] - n_arr[i])

        if temp_l <= temp_r:
            c.append(m_arr[left - 1])
        else:
            c.append(m_arr[left])

    print(sum(c))