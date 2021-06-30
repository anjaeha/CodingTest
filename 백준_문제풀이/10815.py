import sys
input = sys.stdin.readline

n = int(input())
n_arr = sorted(list(map(int, input().split())))

m = int(input())
m_arr = list(map(int, input().split()))


for i in m_arr:
    left = 0
    right = n - 1
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if i == n_arr[mid]:
            answer = 1
            break
        elif i >= n_arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    print(answer, end = ' ')