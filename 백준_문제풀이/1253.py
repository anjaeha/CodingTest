n = int(input())
arr = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    s = arr[:i] + arr[i + 1:]
    left = 0
    right = n - 2

    while left < right:
        temp = s[left] + s[right]

        if temp == arr[i]:
            result += 1
            break

        if temp < arr[i]:
            left += 1
        else:
            right -= 1

print(result)