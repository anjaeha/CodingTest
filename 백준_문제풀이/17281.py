import sys
input = sys.stdin.readline

  
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

visit = [False] * 9
visit[0] = True
batters = [i for i in range(9)]
temp = []

result = 0

def dfs(depth):
    global result
    if depth == 8:
        order = temp[:3] + [0] + temp[3:]
        hitter = -1
        score = 0
        for inning in array:
            out_cnt = 0
            b1, b2, b3 = 0, 0, 0
            while out_cnt < 3:
                hitter = (hitter + 1) % 9
                if inning[order[hitter]] == 0:
                    out_cnt += 1
                elif inning[order[hitter]] == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif inning[order[hitter]] == 2:
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif inning[order[hitter]] == 3:
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                elif inning[order[hitter]] == 4:
                    score += b1 + b2 + b3 + 1
                    b1, b2, b3 = 0, 0, 0
        if result < score:
            result = score
        return

    for i in range(1, 9):
        if visit[i]:
            continue
        
        visit[i] = True
        temp.append(batters[i])
        dfs(depth + 1)
        temp.pop()
        visit[i] = False


  
dfs(0)
print(result)