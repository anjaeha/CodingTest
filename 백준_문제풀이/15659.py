n = int(input())
number = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

MAX = -1000000001
MIN = 1000000001

def dfs(exp, idx, plus, minus, mul, div):
    global MAX, MIN

    if idx == n:
        MAX = max(MAX, eval(exp))
        MIN = min(MIN, eval(exp))
        return

    if plus:
        dfs(exp + '+' + str(number[idx]), idx + 1, plus - 1, minus, mul, div)
    if minus:
        dfs(exp + '-' + str(number[idx]), idx + 1, plus, minus - 1, mul, div)
    if mul:
        dfs(exp + '*' + str(number[idx]), idx + 1, plus, minus, mul - 1, div)
    if div:
        dfs(exp + '//' + str(number[idx]), idx + 1, plus, minus, mul, div - 1)

dfs(str(number[0]), 1, plus, minus, mul, div)
print(MAX)
print(MIN)