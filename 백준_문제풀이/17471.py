from collections import deque

def make_candi(cnt):
    global idx
    if cnt == idx:
        candi.append(list(temp))
        s = []
        for i in range(n):
            if i not in temp:
              s.append(i)
        reverse_candi.append(list(s))
        return


    for i in range(n):
        if not visit[i]:
            temp.append(i)
            visit[i] = True
            make_candi(cnt + 1)
            temp.pop()
            for j in range(i + 1, n):
                visit[j] = False

n = int(input())
people = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(temp[0]):
        graph[i].append(temp[1 + j] - 1)

candi = []
reverse_candi = []
for i in range(1, n // 2 + 1):
    temp = []
    visit = [False] * n
    idx = i
    make_candi(0)

def connect(arr): # 배열안에 원소들이 다 연결되어있는지 확인
    q = deque()
    q.append(arr[0])
    visit = [False] * n
    visit[arr[0]] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visit[i] and i in arr:
                visit[i] = True
                q.append(i)
    for i in arr:
        if not visit[i]:
            return False
    return True

MIN = int(1e9)
for i in range(len(candi)):
    if connect(candi[i]) and connect(reverse_candi[i]):
        left = 0
        right = 0
        for j in range(len(candi[i])):
            left += people[candi[i][j]]
        for j in range(len(reverse_candi[i])):
            right += people[reverse_candi[i][j]]
        MIN = min(abs(left - right), MIN)

print(MIN if MIN != int(1e9) else -1)