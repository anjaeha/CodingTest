n, m, h = map(int, input().split()) # 세로선의 개수, 가로선의 개수, 가로선을 놓을 수 있는 위치의 개수

graph = [[False] * n for _ in range(h)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = True

# 사다리게임의 조건을 만족하는지
def check():
    for idx in range(n):
        k = idx
        for i in range(h):
            if graph[i][k]:
                k += 1
            elif k > 0 and graph[i][k - 1]:
                k -= 1
        if idx != k:
            return False
    return True
        
# 모든 지역에서 사다리 추가해보기
def dfs(depth, x, y):
    global result
    if check():
        result = min(result, depth)
        return
    
    if depth == 3 or result <= depth:
        return
    
    for i in range(x, h):
        if i == x:  # i가 x와 같으면 (x, y)부터 시작하여 사다리를 그어주고
            k = y
        else: # 아니라면 (x, 0)부터 사다리를 그어주는 방식이다.
            k = 0
        
        for j in range(k, n - 1):
            if not graph[i][j] and not graph[i][j + 1]:
                graph[i][j] = True
                dfs(depth + 1, i, j + 2)
                graph[i][j] = False

result = 4
dfs(0, 0, 0)
print(result if result != 4 else -1)