from copy import deepcopy
T = int(input())

def check(): # 보호 필름 성능 테스트
    for i in range(m):
        flag = False
        arr = []
        for j in range(n):
            arr.append(graph[j][i])
        
        for j in range(n - k + 1):
            cnt = 1
            for d in range(j + 1, j + k):
                if arr[j] == arr[d]:
                   cnt += 1 
                else:
                    break
            if cnt >= k:
                flag = True
                break

        if not flag:
            return False
    return True


def make_candi(depth): # 용액을 뿌릴 수 있는 경우의 수 구하기
    global result, temp
    if depth == result:
        candi.append(list(temp))
        return
    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(i)
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, n):
            visit[j] = False

for case in range(1, T + 1):
    n, m, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    while 1:
        visit = [False] * n
        candi = []
        temp = []
        make_candi(0)
        temp_graph = deepcopy(graph)
        for i in range(len(candi)):
            for j in range(result):
                for c in range(m):
                    graph[candi[i][j]][c] = 0
            flag = check()
            if flag:
                break
            for j in range(result):
                for c in range(m):
                    graph[candi[i][j]][c] = 1
            flag = check()
            if flag:
                break
            # 한줄은 A, 한줄은 B를 할 경우를 고려해야함.
            for j in range(0, result // 2):
                for c in range(m):
                    graph[candi[i][j]][c] = 0
            for j in range(result // 2, result):
                for c in range(m):
                    graph[candi[i][j]][c] = 1
            flag  = check()
            if flag:
                break
            for j in range(0, result // 2):
                for c in range(m):
                    graph[candi[i][j]][c] = 1
            for j in range(result // 2, result):
                for c in range(m):
                    graph[candi[i][j]][c] = 0
            if result >= 3:
                for j in range(0, result // 2 + 1):
                    for c in range(m):
                        graph[candi[i][j]][c] = 0
                for j in range(result // 2 + 1, result):
                    for c in range(m):
                        graph[candi[i][j]][c] = 1
                flag  = check()
                if flag:
                    break
                for j in range(0, result // 2 + 1):
                    for c in range(m):
                        graph[candi[i][j]][c] = 0
                for j in range(result // 2 + 1, result):
                    for c in range(m):
                        graph[candi[i][j]][c] = 1
                flag  = check()
                if flag:
                    break
            flag = check()
            if flag:
                break
            graph = deepcopy(temp_graph)

        if flag:
            break
        result += 1

    print("#%d %d" %(case, result))