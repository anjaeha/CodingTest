n, m, k = map(int, input().split()) # N * N 크기의 배열, 나무의 개수 M, K년 후 나무의 숫자
serve = [list(map(int, input().split())) for _ in range(n)] # 추가되는 양분
food = [[5] * n for _ in range(n)] # 양분의 양
trees = [[[] for _ in range(n)] for _ in range(n)] # 나무의 상태

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    x, y, z = map(int, input().split()) # 좌표(x, y), 나이 z
    trees[x - 1][y - 1].append(z)

# 봄 - 어린 나무부터 자신의 나이만큼 양분 먹고 나이 + 1 / 못먹으면 죽음
# 여름 - 봄의 죽은 나무가 양분으로 변함 - 나이 // 2
# 가을 - 나이가 5의 배수면 인접한 8칸에 번식 (나이 1)
# 겨울 - 땅에 양분을 추가

for year in range(k):
    new_food = [i[:] for i in food]
    new_trees = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if trees[x][y]:
               for idx in trees[x][y]:
                   if food[x][y] >= idx:
                       food[x][y] -= idx
                       new_food[x][y] -= idx
                       new_trees[x][y].append(idx + 1)
                   else:
                       new_food[x][y] += idx // 2
            new_food[x][y] += serve[x][y]
    food = new_food
    trees = new_trees

    for x in range(n):
        for y in range(n):
            if trees[x][y]:
               for idx in trees[x][y]:
                   if idx % 5 == 0:
                       for d in range(8):
                           nx = x + dx[d]
                           ny = y + dy[d]

                           if 0 <= nx < n and 0 <= ny < n:
                               trees[nx][ny].insert(0, 1)

result = 0
for x in range(n):
    for y in range(n):
        if trees[x][y]:
            result += len(trees[x][y])
print(result)