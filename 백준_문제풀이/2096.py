import sys
input = sys.stdin.readline

n = int(input())

arr = []
arr_max = [[0, 0, 0], [0, 0, 0]]
arr_min = [[0, 0, 0], [0, 0, 0]]

for _ in range(n):
    temp = list(map(int, input().split()))
    
    arr_max[1][0] = max(arr_max[0][1], arr_max[0][0]) + temp[0]
    arr_max[1][1] = max(arr_max[0][1], arr_max[0][2], arr_max[0][0]) + temp[1]
    arr_max[1][2] = max(arr_max[0][1], arr_max[0][2]) + temp[2]

    arr_min[1][0] = min(arr_min[0][1], arr_min[0][0]) + temp[0]
    arr_min[1][1] = min(arr_min[0][1], arr_min[0][2], arr_min[0][0]) + temp[1]
    arr_min[1][2] = min(arr_min[0][1], arr_min[0][2]) + temp[2]

    arr_max.append(arr_max.pop(0))
    arr_min.append(arr_min.pop(0))

print(max(arr_max[0]), min(arr_min[0]))