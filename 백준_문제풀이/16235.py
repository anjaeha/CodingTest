dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# N * N 의 땅 크기, M개의 나무 구해옴, K년 이후 나무의 개수
n, m, k = map(int, input().split())
# 겨울에 추가하는 양분의 양
graph = [list(map(int, input().split())) for _ in range(n)]

# 초기 양분의 양
eat_tree = [[5] * n for _ in range(n)]

# 나무 상태
pos = [[[] * n for _ in range(n)] for _ in range(n)]

# 사온 나무의 x좌표, y좌표, 나이
for i in range(m):
    x, y, age = map(int, input().split())
    x -= 1
    y -= 1
    pos[x][y].append(age)

# K년 반복
for case in range(k):
    for i in range(n):
        for j in range(n):
            # 값이 들어있으면
            if pos[i][j]:
                dead_tree = 0
                temp_tree = []
                # 봄
                for tmp in pos[i][j]:
                    if tmp <= eat_tree[i][j]:
                        eat_tree[i][j] -= tmp
                        tmp += 1
                        temp_tree.append(tmp)
                    else:
                    	# 실패하면 여름
                        dead_tree += tmp // 2
                eat_tree[i][j] += dead_tree
                pos[i][j] = []
                pos[i][j].extend(temp_tree)


    for i in range(n):
        for j in range(n):
        	# 겨울
            eat_tree[i][j] += graph[i][j]
            if pos[i][j]:
                if pos[i][j][-1] == -1:
                    continue
                for temp in range(len(pos[i][j])):
                    if pos[i][j][temp] < 0:
                        continue
                    # 가을
                    if pos[i][j][temp] % 5 == 0:
                        for d in range(8):
                            nx = i + dx[d]
                            ny = j + dy[d]

                            if 0 <= nx < n and 0 <= ny < n:
                                pos[nx][ny].insert(0, 1)
            

result = 0
for i in range(n):
    for j in range(n):
        for t in range(len(pos[i][j])):
            if pos[i][j][t] > 0:
                result += 1

print(result)