import sys
import copy
input = sys.stdin.readline

n = int(input())
arr =  [list(map(int, input().split())) for _ in range(n)]
result = 0

def move(idx):
    if idx == 0:
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[idx][j] == 0:
                        arr[idx][j] = temp
                    elif arr[idx][j] == temp:
                        arr[idx][j] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        arr[idx][j] = temp

    elif idx == 1:
        for j in range(n):
            idx = n - 1
            for i in range(n - 2, -1, -1):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[idx][j] == 0:
                        arr[idx][j] = temp
                    elif arr[idx][j] == temp:
                        arr[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[idx][j] = temp

    elif idx == 2:
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = temp
                    elif arr[i][idx] == temp:
                        arr[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        arr[i][idx] = temp

    else:
        for i in range(n):
            idx = n - 1
            for j in range(n - 2, -1, -1):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = temp
                    elif arr[i][idx] == temp:
                        arr[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[i][idx] = temp


def dfs(cnt):
    global result, arr
    if cnt == 5:
        for i in range(n):
            result = max(result, max(arr[i]))
        return

    tmp = copy.deepcopy(arr)
    
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        arr = copy.deepcopy(tmp)

dfs(0)
print(result)