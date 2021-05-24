import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

s = []
for i in range(N):
    s.append(list(map(int, input().split())))

for rr in range(R):
    x, y = 0, 0
    n, m = N, M

    for case in range(min(N, M) // 2):
        
        tmp = s[x][y]

        for i in range(m-1): #위
            s[x][y+i] = s[x][y+i+1]

        for i in range(n-1): #오른쪽
            s[x+i][y+m-1] = s[x+i+1][y+m-1]

        for i in range(m-1): #아래
            s[x+n-1][y+m-1-i] = s[x+n-1][y+m-2-i]

        for i in range(n-1): #왼쪽
            s[x+n-i-1][y] = s[x+n-i-2][y]

        s[x+1][y] = tmp

        n -= 2
        m -= 2
        
        x += 1
        y += 1


for i in s:
    print(*i)