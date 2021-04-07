import sys
input = sys.stdin.readline

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

m_cnt = 0
z_cnt = 0
p_cnt = 0

def cut(x, y, n):
    global m_cnt, z_cnt, p_cnt
    check = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                cut(x, y, n // 3)
                cut(x + n // 3, y, n // 3)
                cut(x + (n // 3 * 2), y, n // 3)
                cut(x, y + n // 3, n // 3)
                cut(x + n // 3, y + n // 3, n // 3)
                cut(x + n // 3, y + (n // 3 * 2), n // 3)
                cut(x , y +  (n // 3 * 2), n // 3)
                cut(x + (n // 3 * 2), y + n // 3, n // 3)
                cut(x + ( n // 3 * 2), y + (n // 3 * 2), n //3 )
                return



    if check == -1:
        m_cnt += 1
        return
    elif check == 0:
        z_cnt += 1
        return
    else:
        p_cnt += 1
        return



cut(0, 0, n)
print(m_cnt)
print(z_cnt)
print(p_cnt)
