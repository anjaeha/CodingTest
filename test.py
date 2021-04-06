n = int(input())

s = []
for i in range(n):
    s.append(list(map(int, input().split())))

white = 0
blue = 0

def cut(x, y, n):
    global blue, white
    check = s[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != s[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return
    
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return

cut(0, 0, n)
print(white)
print(blue)

