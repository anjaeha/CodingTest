n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def check(arr):
    visit = [False] * n  # 경사로
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            continue

        if abs(arr[i] - arr[i + 1]) > 1:
            return False

        if arr[i] > arr[i + 1]:  # 왼쪽이 더 크면 오른쪽에 경사로 설치해줘야함
            if i + l < n:
                for j in range(i + 1, i + 1 + l):
                    if not visit[j] and arr[j] == arr[i + 1]:
                        visit[j] = True
                    else:
                        return False
            else:
                return False
        else:  # 오른쪽이 더 크면 왼쪽에 경사로 설치해줘야함
            if i - l + 1 >= 0:
                for j in range(i, i - l, -1):
                    if not visit[j] and arr[j] == arr[i]:
                        visit[j] = True
                    else:
                        return False
            else:
                return False
    return True


result = 0
for i in range(n):
    if check(graph[i]):
        result += 1

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(graph[j][i])
    if check(temp):
        result += 1
print(result)