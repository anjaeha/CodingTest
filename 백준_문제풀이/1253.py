import sys
input = sys.stdin.readline

n = int(input())
s = sorted(list(map(int, input().split())))
cnt = 0

for i in range(n):
    arr = s[:i] +s[i+1:] # 해당 숫자를 제외한 다른 두 수의 합으로 만들어야해서 빼주는 과정, 0이 들어가있을 경우 0 + x 로 x 를 만들어버림.
    left = 0
    right = n - 2

    while left < right:
        check = arr[left] + arr[right]

        if check == s[i]:
            cnt += 1
            break

        if check < s[i]:
            left += 1
        else:
            right -= 1

print(cnt)