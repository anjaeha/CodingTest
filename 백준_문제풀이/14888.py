import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
plus, sub, mul, div = map(int, input().split())

def dfs(cnt, result, p, s, m, d):
    global max_result, min_result

    if cnt == n:
        max_result = max(result, max_result)
        min_result = min(result, min_result)

    if p:
        dfs(cnt + 1, result + number[cnt], p - 1, s, m, d)
    if s:
        dfs(cnt + 1, result - number[cnt], p, s - 1, m, d)
    if m:
        dfs(cnt + 1, result * number[cnt], p, s, m - 1, d)
    if d:
        dfs(cnt + 1, result // number[cnt] if result > 0 else -(-result // number[cnt]), p, s, m, d - 1)


max_result = -1000000001
min_result = 1000000001

dfs(1, number[0], plus, sub, mul, div)
print(max_result)
print(min_result)