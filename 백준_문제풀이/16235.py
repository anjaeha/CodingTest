n, m, k = map(int, input().split()) # N * N 크기, 심은 나무의 개수 M, K년후 나무의 개수 구하기
food = [[5] * n for _ in range(n)] # 원래 양분
add_food = [list(map(int, input().split())) for _ in range(n)] # 추가 양분
trees = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def season():
    for x in range(n):
        for y in range(n):
            if trees[x][y]:
                temp = []
                dead = 0
                for c in range(len(trees[x][y])):
                    if food[x][y] >= trees[x][y][c]:
                        food[x][y] -= trees[x][y][c]
                        temp.append(trees[x][y][c] + 1)
                    else:
                        dead += trees[x][y][c] // 2
                trees[x][y] = temp
                food[x][y] += dead

    for x in range(n):
        for y in range(n):
            food[x][y] += add_food[x][y]
            if trees[x][y]:
                for c in range(len(trees[x][y])):
                    if trees[x][y][c] % 5 == 0:
                        for d in range(8):
                            nx = x + dx[d]
                            ny = y + dy[d]

                            if 0 <= nx < n and 0 <= ny < n:
                                trees[nx][ny].insert(0, 1)


for _ in range(k):
    season()

result = 0
for i in range(n):
    for j in range(n):
        result += len(trees[i][j])

print(result)