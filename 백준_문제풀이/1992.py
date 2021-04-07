n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input())))


answer = []

def cut(x, y, n):
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                answer.append('(')
                cut(x, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                answer.append(')')
                return

    if check == 1:
        answer.append(1)
    else:
        answer.append(0)
    

cut(0, 0, n)

for i in answer:
    print(i, end = '')