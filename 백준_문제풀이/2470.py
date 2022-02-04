n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = []
left = 0
right = n - 1

while left < right:
    temp = arr[left] + arr[right]
    if answer:
        if abs(temp) < abs(sum(answer)):
            answer = [arr[left], arr[right]]
    else:
        answer = [arr[left], arr[right]]

    if temp < 0:
        left += 1
    else:
        right -= 1

print(*answer)