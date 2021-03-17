N = int(input())
arr = list(map(int, input().split()))

print(max(arr)  * min(arr))

# 1과 N을 제외한 모든 약수가 주어져서 최대값과 최소값 곱하면 끝