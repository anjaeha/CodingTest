T = int(input())

for case in range(T):
    a, b = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    arr_a.sort()
    arr_b.sort()

    answer = 0

    for i in range(a):
        s = arr_a[i]
        left = 0
        right = b - 1

        while left <= right:
            mid = (left + right) // 2
            if arr_b[mid] < s:
                left = mid + 1
            else:
                right = mid - 1

        answer += left

    print(answer)