import sys, copy
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

def move(idx):
    if idx == 0:
        for i in range(n):
            q = []
            for j in range(n):
                if arr[i][j]:
                    q.append(arr[i][j])
                    arr[i][j] = 0
            answer = []
            while q:
                temp = q.pop(0)
                if q:
                    if temp == q[0]:
                        answer.append(temp * 2)
                        q.pop(0)
                    else:
                        answer.append(temp)
                else:
                    answer.append(temp)
            for j in range(n):
                if answer:
                    arr[i][j] = answer.pop(0)
                
    elif idx == 1:
        for i in range(n):
            q = []
            for j in range(n-1, -1, -1):
                if arr[i][j]:
                    q.append(arr[i][j])
                    arr[i][j] = 0
            answer = []
            while q:
                temp = q.pop(0)
                if q:
                    if temp == q[0]:
                        answer.append(temp * 2)
                        q.pop(0)
                    else:
                        answer.append(temp)
                else:
                    answer.append(temp)
            for j in range(n-1, -1, -1):
                if answer:
                    arr[i][j] = answer.pop(0)
                    
    elif idx == 2:
        for i in range(n):
            q = []
            for j in range(n):
                if arr[j][i]:
                    q.append(arr[j][i])
                    arr[j][i] = 0
            answer = []
            while q:
                temp = q.pop(0)
                if q:
                    if temp == q[0]:
                        answer.append(temp * 2)
                        q.pop(0)
                    else:
                        answer.append(temp)
                else:
                    answer.append(temp)
            for j in range(n):
                if answer:
                    arr[j][i] = answer.pop(0)

    elif idx == 3:
        for i in range(n):
            q = []
            for j in range(n-1, -1, -1):
                if arr[j][i]:
                    q.append(arr[j][i])
                    arr[j][i] = 0
            answer = []
            while q:
                temp = q.pop(0)
                if q:
                    if temp == q[0]:
                        answer.append(temp * 2)
                        q.pop(0)
                    else:
                        answer.append(temp)
                else:
                    answer.append(temp)
            for j in range(n-1, -1, -1):
                if answer:
                    arr[j][i] = answer.pop(0)


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