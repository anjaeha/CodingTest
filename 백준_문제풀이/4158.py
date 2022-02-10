# 상근이 CD의 수 N, 선영이 CD의 수 M
# N, M <= 10000000
# N개의 줄에 상근이가 가지고 있는 CD의 번호, M개의 줄에 선영이가 가지고 있는 CD의 번호
# 마짐가줄에는 0, 0
# 두 사람이 동시에 가지고 있는 CD의 개수 출력
import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    arr = [int(input()) for _ in range(n)]

    result = 0
    for i in range(m):
       x = int(input())

       left = 0
       right = n - 1

       while left <= right:
           mid = (left + right) // 2
           if arr[mid] == x:
               result += 1
               break

           elif arr[mid] < x:
               left = mid + 1
           else:
               right = mid - 1

    print(result)