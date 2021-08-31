
def check1():
    n = len(graph)
    m = len(graph[0])
    array = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            array[i][j] = graph[n-i-1][j]
    return array

def check2():
    n = len(graph)
    m = len(graph[0])
    array = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            array[i][j] = graph[i][m - j - 1]
    return array

def check3():
    n = len(graph)
    m = len(graph[0])
    array = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            array[j][i] = graph[n - 1 -i][j]
    return array


def check4():
    n = len(graph)
    m = len(graph[0])
    array = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            array[j][i] = graph[i][m - 1 - j]
    return array    


def check5():
    n = len(graph)
    m = len(graph[0])
    array = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i < n // 2 and j < m // 2:
                array[i][j] = graph[n // 2 + i][j]
            elif i < n // 2 and j >= m // 2:
                array[i][j] = graph[i][j - m // 2]
            elif i >= n // 2 and j < m // 2:
                array[i][j] = graph[i][m // 2 + j]
            elif i >= n // 2 and j >= m // 2:
                array[i][j] = graph[i - n // 2][j]
    return array

def check6():
    n = len(graph)
    m = len(graph[0])
    array = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i < n // 2 and j < m // 2:
                array[i][j] = graph[i][j + m // 2]
            elif i < n // 2 and j >= m // 2:
                array[i][j] = graph[i + n // 2][j]
            elif i >= n // 2 and j < m // 2:
                array[i][j] = graph[i - n // 2][j]
            elif i >= n // 2 and j >= m // 2:
                array[i][j] = graph[i][j - m // 2]
    return array

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cal = list(map(int, input().split()))

for case in range(r):
    if cal[case] == 1:
        graph = check1()
    elif cal[case] == 2:
        graph = check2()
    elif cal[case] == 3:
        graph = check3()
    elif cal[case] == 4:
        graph = check4()
    elif cal[case] == 5:
        graph = check5()
    elif cal[case] == 6:
        graph = check6()

for i in graph:
    print(*i)