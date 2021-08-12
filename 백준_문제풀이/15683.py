import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())
dir = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[2, 0], [2, 1], [0, 3], [3, 1]], [[2, 0, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]], [[0, 1, 2, 3]]]
s = []
q = []
cctv_cnt = 0
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(len(a)):
        if a[j] in (1,2,3,4,5):
            q.append([i, j, a[j]])
            cctv_cnt += 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0 ,0]

def fill(x, y, arr, d):
    for i in d:
        nx, ny = x, y
        while 1:
            nx += dx[i]
            ny += dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = '#'
                elif arr[nx][ny] == 6:
                    break
            else:
                break

result = sys.maxsize
def dfs(arr, cnt):
    global result
    tmp = copy.deepcopy(arr)
    if cnt == cctv_cnt:
        temp = 0
        for i in range(n):
            temp += tmp[i].count(0)
        result = min(result, temp)
        return

    
    x, y, cctv = q[cnt]
    for i in dir[cctv]:
        fill(x, y, tmp, i)
        dfs(tmp, cnt + 1)
        tmp = copy.deepcopy(arr)
    
dfs(s, 0)
print(result)

#브루트 포스 관련 문제 풀어보기!