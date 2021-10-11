T = int(input())

def calc(depth, temp, pl, mi, mu, di):
    global MAX, MIN
    if depth == n:
        MAX = max(MAX, temp)
        MIN = min(MIN, temp)
        return

    if pl:
        calc(depth + 1, temp + number[depth], pl - 1, mi, mu, di)
    if mi:
        calc(depth + 1, temp - number[depth], pl, mi - 1, mu, di)
    if mu:
        calc(depth + 1, temp * number[depth], pl, mi, mu - 1, di)
    if di:
        calc(depth + 1, temp // number[depth] if temp >= 0 else -(-temp // number[depth]), pl, mi, mu, di - 1)


for tc in range(1, T + 1):
    n = int(input())
    plus, minus, multi, div = map(int, input().split())
    number = list(map(int, input().split()))
    MAX = -100000001
    MIN = 100000001
    calc(1, number[0], plus, minus, multi, div)

    print("#%d %d" %(tc, MAX - MIN))