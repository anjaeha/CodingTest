import sys
input = sys.stdin.readline

n = int(input())

a, b, c = [False] * n, [False] * (2*n-1), [False] * (2*n-1)
# 직선, / 대각선, \ 대각선

cnt = 0
def solve(i):
    global cnt
    if i == n: # 행 끝까지..
        cnt += 1
        return

    for j in range(n): # 열 이동
        if (a[j] or b[i+j] or c[i-j+n-1]) == False:
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False



solve(0)
print(cnt)