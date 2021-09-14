
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def check(arr):
    visit = [False] * n

    for i in range(n - 1):
        # 현재랑 다음꺼랑 같은지 확인
        if arr[i] == arr[i + 1]:
            continue

        # 현재랑 다음꺼랑 다른데 1이상 차이나면 실패
        if abs(arr[i] - arr[i + 1]) > 1:
            return False

        # 만약 왼쪽이 큰 값이면
        if arr[i] > arr[i + 1]:
            temp = arr[i + 1]
            for j in range(i + 1, i + 1 + l):
                # 주어진 그래프를 벗어나면
                if j < 0 or j >= n:
                    return False
                # 경사로 설치했으면
                if visit[j]:
                    return False
                # l의 크기만큼 길이 길지 않으면
                if temp != arr[j]:
                    return False
                # 경사로 설치
                visit[j] = True
        else:
            temp = arr[i]
            for j in range(i, i - l, -1):
                if j < 0 or j >= n:
                    return False
                if visit[j]:
                    return False
                if temp != arr[j]:
                    return False
                visit[j] = True      

    return True

result = 0
# 행 검사
for i in range(n):
    if check(graph[i]):
        result += 1

# 열 검사
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(graph[j][i])
    if check(temp):
        result += 1

print(result)