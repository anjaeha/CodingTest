def move(idx, score):
    global max_score

    if idx == 10:
        if score > max_score:
            max_score = score
        return

    num = dices[idx]

    for i in range(32):
        if positions[i]:
            nx = moving[i][num - 1]
            if positions[nx]:
                continue
            
            positions[i].pop()
            if nx == 32:
                move(idx + 1, score)
            else:
                positions[nx].append(1)
                move(idx + 1, score + scores[nx])
                positions[nx].pop()
            positions[i].append(1)


positions = [[] for _ in range(33)]
positions[0] = [1, 1, 1, 1]

moving = {
    0: [1, 2, 3, 4, 5],
    1: [2, 3, 4, 5, 6],
    2: [3, 4, 5, 6, 7],
    3: [4, 5, 6, 7, 8],
    4: [5, 6, 7, 8, 9],
    5: [21, 22, 23, 29, 30],
    6: [7, 8, 9, 10, 11],
    7: [8, 9, 10, 11, 12],
    8: [9, 10, 11, 12, 13],
    9: [10, 11, 12, 13, 14],
    10: [24, 25, 29, 30, 31],
    11: [12, 13, 14, 15, 16],
    12: [13, 14, 15, 16, 17],
    13: [14, 15, 16, 17, 18],
    14: [15, 16, 17, 18, 19],
    15: [26, 27, 28, 29, 30],
    16: [17, 18, 19, 20, 32],
    17: [18, 19, 20, 32, 32],
    18: [19, 20, 32, 32, 32],
    19: [20, 32, 32, 32, 32],
    20: [32, 32, 32, 32, 32],
    21: [22, 23, 29, 30, 31],
    22: [23, 29, 30, 31, 20],
    23: [29, 30, 31, 20, 32],
    24: [25, 29, 30, 31, 20],
    25: [29, 30, 31, 20, 32],
    26: [27, 28, 29, 30, 31],
    27: [28, 29, 30, 31, 20],
    28: [29, 30, 31, 20, 32],
    29: [30, 31, 20, 32, 32],
    30: [31, 20, 32, 32, 32],
    31: [20, 32, 32, 32, 32],
}

scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0]

dices = list(map(int, input().split()))
max_score = 0
move(0, 0)
print(max_score)

"""
from copy import deepcopy

a = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0], [10, 13, 16, 19, 25, 30, 35, 40, 0], [30, 28, 27, 26, 25, 30, 35, 40, 0], [20, 22, 24, 25, 30, 35, 40, 0]]
# 테두리 21개, 1번 8개, 2번 8개, 3번 7개

move = list(map(int, input().split()))
piece = [0] * 10
result = -1
def dfs(depth):
    global result
    if depth == 10:
        # move하는 말을 piece에 담은 상태
        yut = [0] * 5 # 윷의 현재 위치
        temp = 0 # 말이 이동했을때 점수를 받기 위함
        d = [0] * 5 # 어디방향으로 돌고 있는지

        for i in range(10): # 말 이동 시작
            x = piece[i] # 어떤말이 이동하는지
            go = move[i] # 몇칸 이동하는지
            yut[x] += go
            

            if d[x] == 0 and yut[x] >= 21:
                yut[x] = 21
                continue
            elif d[x] == 1 and yut[x] >= 8:
                yut[x] = 8
                continue
            elif d[x] == 2 and yut[x] >= 8:
                yut[x] = 8
                continue
            elif d[x] == 3 and yut[x] >= 7:
                yut[x] = 7
                continue

            # 도착하면
            for j in range(1, 5):
                if x == j: # 본인의 위치를 제외한 다른 윷의 위치가 중복되면 끝
                    continue
                if a[d[x]][yut[x]] == a[d[j]][yut[j]]:
                    if a[d[x]][yut[x]] in [16, 22, 24, 26, 28, 30]: # 여러길에서 오는 25, 30, 35, 40이 중복될수있음
                        if a[d[x]][yut[x]] in [16, 22, 24, 26, 28]:
                            if d[x] == d[j]:
                                return
                        else:
                            if ((d[x] == 0 and yut[x] == 15) and ((d[j] == 1 and yut[j] == 5) or (d[j] == 2 and yut[j] == 5) or (d[j] == 3 and yut[j] == 4)) or ((d[x] == 1 and yut[x] == 5) and (d[j] == 0 and yut[j] == 15))) or ((d[x] == 2 and yut[x] == 5) and (d[j] == 0 and yut[j] == 15)) or ((d[x] == 3 and yut[x] == 4) and (d[j] == 0 and yut[j] == 15)):
                                pass
                            else:
                                return
                    else:
                        return

            if d[x] == 0 and yut[x] == 5: # 5칸 이동해서 10이면
                d[x] = 1
                yut[x] = 0
            elif d[x] == 0 and yut[x] == 10: # 10칸 이동해서 20이면
                d[x] = 3
                yut[x] = 0
            elif d[x] == 0 and yut[x] == 15: # 15칸 이동해서 30이면
                d[x] = 2
                yut[x] = 0
            
            temp += a[d[x]][yut[x]]
        if result < temp:
            result = temp
        return


    for i in range(1, 5): # 어떤말을 이동할지 결정하기 위함
        piece[depth] = i # 1~4번째 말을 이동한다고 결정
        dfs(depth + 1)

dfs(0)
print(result)
89%에서 틀림. 어디가틀린지?
"""