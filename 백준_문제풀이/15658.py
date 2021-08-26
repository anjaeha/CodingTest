import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())

MAX = -sys.maxsize
MIN = sys.maxsize


def dfs(cnt, result, plus, minus, multi, div):
    global MAX, MIN
    if cnt == n:
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return

    if plus:
        dfs(cnt + 1, result + s[cnt], plus - 1, minus, multi, div)
    if minus:
        dfs(cnt + 1, result - s[cnt], plus, minus -1, multi, div)
    if multi:
        dfs(cnt + 1, result * s[cnt], plus, minus, multi - 1, div)
    if div:
        dfs(cnt + 1, result // s[cnt] if result > 0 else -(-result // s[cnt]), plus, minus, multi, div - 1)

dfs(1, s[0], plus, minus, multi, div)


print(MAX)
print(MIN)