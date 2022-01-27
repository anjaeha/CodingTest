from itertools import combinations


def solution(line):
    max_x = -int(1e15)
    min_x = int(1e15)
    max_y = -int(1e15)
    min_y = int(1e15)
    point = []
    x_list, y_list = [], []

    for x, y in list(combinations(line, 2)):
        A, B, E = x
        C, D, F = y

        if A * D - B * C == 0:
            continue

        nx = (B * F - E * D) / (A * D - B * C)
        ny = (E * C - A * F) / (A * D - B * C)

        if nx == int(nx) and ny == int(ny):
            point.append((int(nx), int(ny)))
            x_list.append(int(nx))
            y_list.append(int(ny))

    max_x, min_x = max(x_list), min(x_list)
    max_y, min_y = max(y_list), min(y_list)

    length_x = max_x - min_x + 1
    length_y = max_y - min_y + 1

    answer = [['.'] * length_x for _ in range(length_y)]

    for x, y in point:
        answer[max_y - y][x - min_x] = '*'

    result = []
    for i in answer:
        result.append(''.join(i))

    return result