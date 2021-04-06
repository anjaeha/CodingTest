n = int(input())

paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

white = 0
blue = 0

def solution(x, y, n):
    global white, blue
    check = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y+ n):
            if check != paper[i][j]:
                solution(x, y, n // 2)
                solution(x + n // 2, y, n // 2)
                solution(x, y + n // 2, n // 2)
                solution(x + n//2, y + n//2, n // 2)
                return

    if check == 0:
        white += 1
    else:
        blue += 1

solution(0, 0, n)
print(white)
print(blue)