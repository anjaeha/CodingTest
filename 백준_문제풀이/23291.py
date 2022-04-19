from collections import deque
from copy import deepcopy
n, k = map(int, input().split()) # N마리의 물고기, 최대 - 최소가 K 이하
graph = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def min_fish():
    MIN = min(graph)
    for i in range(n):
        if graph[i] == MIN:
            graph[i] += 1

def check():
    MIN = min(graph)
    MAX = max(graph)
    if MAX - MIN <= k:
        return True
    return False


def bowl_organ():
    q = [deque() for _ in range(10)]
    q[0].extend(graph)
    q[1].append(q[0].popleft())
    while 1:
        count = 0
        for idx in range(len(q)):
            if q[idx]:
                count += 1
            else:
                break
        if len(q[0]) - len(q[1]) < count:
            break

        for idx in range(len(q[1]), 0, -1):
            for i in range(count):
                q[idx].append(q[i].popleft())
    return q

def fish_control(q):
    copy_q = deepcopy(q)
    for x in range(len(q)):
        for y in range(len(q[x])):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < len(q) and 0 <= ny < len(q[nx]):
                    if q[x][y] - q[nx][ny] >= 5:
                        copy_q[x][y] -= (q[x][y] - q[nx][ny]) // 5
                        copy_q[nx][ny] += (q[x][y] - q[nx][ny]) // 5
    return copy_q

def arrange(q):
    arr = []
    count = 0
    for idx in range(len(q)):
        if q[idx]:
            count += 1
        else:
            break

    for idx in range(len(q[1])):
        for i in range(count):
            arr.append(q[i].popleft())
    arr.extend(q[0])
    return arr

def build():
    q = [deque() for _ in range(4)]

    arr0 = graph[n//2:]
    arr1= graph[:n//2][::-1]

    q[0].extend(arr0[len(arr0) // 2:])
    q[3].extend(arr0[:len(arr0) // 2][::-1])
    q[1].extend(arr1[len(arr1) // 2:])
    q[2].extend(arr1[:len(arr1) // 2][::-1])

    return q

result = 0
while 1:
    result += 1
    min_fish() # 가장 적은 어항에 물고기 + 1
    q = bowl_organ() # 어항을 쌓는 함수
    q = fish_control(q) # 물고기 수 조절
    graph = arrange(q) # 일렬로 정렬
    q = build() # 4층 높이로 쌓는 정렬
    q = fish_control(q) # 물고기 수 정렬
    graph = arrange(q) # 일렬로 정렬
    if check(): # 종료 조건을 만족하는지
        break

print(result)