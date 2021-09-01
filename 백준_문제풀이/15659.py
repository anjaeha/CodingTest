from copy import deepcopy

n = int(input())
number = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

MAX = -1000000001
MIN = 1000000001

def dfs(answer, idx, cal):
    global MAX, MIN

    if idx == n:
        MAX = max(MAX, eval(answer))
        MIN = min(MIN, eval(answer))
        return
    
    if cal[0] < plus:
        cal[0] += 1
        dfs(answer + '+' + str(number[idx]), idx + 1, cal)
        cal[0] -= 1

    if cal[1] < minus:
        cal[1] += 1
        dfs(answer + '-' + str(number[idx]), idx + 1, cal)
        cal[1] -= 1

    if cal[2] < mul:
        cal[2] += 1
        dfs(answer + '*' + str(number[idx]), idx + 1, cal)
        cal[2] -= 1

    if cal[3] < div:
        cal[3] += 1
        dfs(answer + '//' + str(number[idx]), idx + 1, cal)
        cal[3] -= 1



dfs(str(number[0]), 1, [0, 0, 0, 0])


print(MAX)
print(MIN)