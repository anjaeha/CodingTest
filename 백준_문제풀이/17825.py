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
            
            if d[x] == 0 and yut[x] == 5: # 5칸 이동해서 10이면
                d[x] = 1
                yut[x] = 0
            elif d[x] == 0 and yut[x] == 10: # 10칸 이동해서 20이면
                d[x] = 3
                yut[x] = 0
            elif d[x] == 0 and yut[x] == 15: # 15칸 이동해서 30이면
                d[x] = 2
                yut[x] = 0

            # 도착하면
            for j in range(1, 5):
                if x == j: # 본인의 위치를 제외한 다른 윷의 위치가 중복되면 끝
                    continue
                visit = a[d[x]][yut[x]]
                if visit == a[d[j]][yut[j]]:
                    if visit == 30:
                        if (d[x] == 3 and yut[x] == 0) and (d[j] == 3 and yut[j] == 0):
                            return
                        elif (d[x] != 3 and yut[x] != 0) and (d[j] != 3 and yut[j] != 0):
                            return
                    elif visit in [16, 22, 24, 26, 28]:
                        if d[x] == d[j]:
                            return
                    elif visit == 0:
                        continue
                    else:
                        return

            
            temp += a[d[x]][yut[x]]
        if result < temp:
            result = temp
        return


    for i in range(1, 5): # 어떤말을 이동할지 결정하기 위함
        piece[depth] = i # 1~4번째 말을 이동한다고 결정
        dfs(depth + 1)

dfs(0)
print(result)
