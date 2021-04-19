import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += a[j]

        if sum == m:
            cnt += 1
            continue
        elif sum > m:
            break


print(cnt)

# 수열 A의 i번째  수부터 j번째 수까지의 합이 M이 되는 경우의 수를 찾는 문제이기 때문에
# 2중 for문을 돌려서 i번째부터 i+1, i+2 .. 를 계속 더하여 sum이 m과 같으면 경우의 수 +1을 해준다. 더 크면 더 돌릴 필요가 없기에 break!