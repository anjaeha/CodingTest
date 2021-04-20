import sys
input = sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

for i in range(m):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if n_list[mid] == m_list[i]:
            print(1, end = ' ')
            break

        elif n_list[mid] > m_list[i]:
            right = mid - 1
        else:
            left = mid + 1

        if left > right:
            print(0, end = ' ')
            break

        