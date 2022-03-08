n = int(input()) # 수의 개수
numbers = list(map(int, input().split()))
ps, ms, ml, dv = map(int, input().split())

MAX = -int(1e9)
MIN = int(1e9)

def dfs(depth, result, plus, minus, mul, div):
    global MAX, MIN
    if depth == n:
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return

    if plus:
        dfs(depth + 1, result + numbers[depth], plus - 1, minus, mul, div)

    if minus:
        dfs(depth + 1, result - numbers[depth], plus, minus - 1, mul, div)

    if mul:
        dfs(depth + 1, result * numbers[depth], plus, minus, mul - 1, div)

    if div:
        dfs(depth + 1, result // numbers[depth] if result > 0 else -(-result // numbers[depth]), plus, minus, mul, div - 1)

dfs(1, numbers[0], ps, ms, ml, dv)
print(MAX)
print(MIN)