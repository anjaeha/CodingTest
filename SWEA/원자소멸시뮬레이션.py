"""
2차원 평면에서 이동하며 두 개 이상의 원자가 충돌하면 각자 보유한 에너지를 모두 방출하고 소멸됨
1. 상 - y증가, 하 - y감소, 좌 - x감소, 우 - x증가 (기존에 쓰던 x, y가 바뀜)
2. 이동속도는 동일, 1초에 1만큼 이동
3. 최초의 위치에서 동시에 이동 시작함
4. 두 개 이상의 원자가 동시에 충돌하면 에너지 방출하고 소멸
1 <= N <= 1000
1 <= K <= 100
-1000 <= x, y <= 1000
0상 1하 2좌 3우
이동방향은 바뀌지 않음
"""
def check():
    temp = 0
    for rc, val in atom.items():
        temp += 1
    if temp >= 2:
        return True
    else:
        return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] # 기존에서 x와 y의 위치를 바꿈 x를 y로, y를 x로

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    atom = {}
    for _ in range(n):
        y, x, d, k = map(int, input().split()) # x위치, y위치, 이동 방향, 보유에너지K
        atom[(-x * 2, y * 2)] = [d, k]
    # 충돌하거나, 범위를 벗어나거나 둘 중 하나를 해야함.
    result = 0

    for _ in range(4002): # 0.5 씩 이동
        if not check(): # 없어도 문제 통과 되긴하는데, 1개 남았을 경우에는 어차피 충돌못하기때문에 끝내주는것이 맞는거같음.
            break
        new_atom = {}
        crush = {}
        for rc, val in atom.items():
            x, y, d, k = rc[0], rc[1], val[0], val[1]
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < -2000 or ny < -2000 or nx > 2000 or ny > 2000:
                continue

            if ((nx, ny)) not in new_atom:
                new_atom[(nx, ny)] = [d, k]
            else:
                result += k
                temp = new_atom[(nx, ny)][1]
                new_atom[(nx, ny)][1] = 0
                result += temp
                if ((nx, ny)) not in crush:
                    crush[(nx, ny)] = 1

        for nxy, value in crush.items():
            del new_atom[(nxy[0], nxy[1])]
        atom = new_atom

    print("#%d %d" %(tc, result))