a, b, c = map(int, input().split())

def solve(x ,y):
    if y % 2 == 1:
        return solve(x, y - 1) * x
    elif y == 1:
        return x
    elif y == 0:
        return 1
    else:
        result = solve(x, y // 2)
        return result ** 2 % c


print(solve(a, b) % c)