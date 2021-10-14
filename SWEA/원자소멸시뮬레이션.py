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


dx = [-0.5, 0.5, 0, 0]
dy = [0, 0, -0.5, 0.5] # 기존에서 x와 y의 위치를 바꿈 x를 y로, y를 x로

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    atom = {}
    for _ in range(n):
        y, x, d, k = map(int, input().split()) # x위치, y위치, 이동 방향, 보유에너지K
        atom[(-x, y)] = [d, k]
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
            if nx < -1000 or ny < -1000 or nx > 1000 or ny > 1000:
                continue

            if new_atom.get((nx, ny)) is None:
                new_atom[(nx, ny)] = [d, k]
            else:
                result += k
                temp = new_atom[(nx, ny)][1]
                new_atom[(nx, ny)][1] = 0
                result += temp
                if crush.get((nx, ny)) is None:
                    crush[(nx, ny)] = 1

        for nxy, value in crush.items():
            new_atom.pop((nxy[0], nxy[1]))
        atom = new_atom

    print("#%d %d" %(tc, result))