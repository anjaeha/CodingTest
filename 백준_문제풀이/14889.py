n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visit = [False] * n
candi = []
temp = []
def make_candi(depth):
    if depth == n // 2:
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
make_candi(0)

def score(arr):
    stat = 0
    for x in arr:
        for y in arr:
            stat += graph[x][y]
    return stat

result = int(1e9)
for idx in range(len(candi)):
    right = candi[idx]
    left = []
    for i in range(n):
        if i not in right:
            left.append(i)
    # 두 팀으로 나눔
    r_score = score(right)
    l_score = score(left)
    result = min(result, abs(r_score - l_score))

print(result)