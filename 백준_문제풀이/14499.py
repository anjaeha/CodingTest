import sys
input = sys.stdin.readline

"""
동          서            남             북
1 -> 3      1 -> 4        1 -> 2           1 -> 5
2 -> 2      2 -> 2        2 -> 6           2 -> 1
3 -> 6      3 -> 1        3 -> 3           3 -> 3
4 -> 1      4 -> 6        4 -> 4           4 -> 4
5 -> 5      5 -> 5        5 -> 1           5 -> 6
6 -> 4      6 -> 3        6 -> 5           6 -> 2  동서는 방향 반대인데 남북은 정상임
"""

def move(n, arr):
    if n == 1: # 동
        return [0, arr[3], arr[2], arr[6], arr[1], arr[5], arr[4]]
    elif n == 2: # 서
        return [0, arr[4], arr[2], arr[1], arr[6], arr[5], arr[3]]
    elif n == 3: # 남
        return [0, arr[2], arr[6], arr[3], arr[4], arr[1], arr[5]]
    elif n == 4: # 북
        return [0, arr[5], arr[1], arr[3], arr[4], arr[6], arr[2]]


n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dice = [0] * 7

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for i in range(k):
    if 0 <= x + dx[order[i]] < n and 0 <= y + dy[order[i]] < m:
        x = x + dx[order[i]]
        y = y + dy[order[i]]

        dice = move(order[i], dice)

        if graph[x][y] == 0:
            graph[x][y] = dice[6]
        else:
            dice[6] = graph[x][y]
            graph[x][y] = 0

        print(dice[1])