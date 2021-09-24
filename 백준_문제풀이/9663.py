# N * N 체스판에 N개의 퀸을 놓을 수 있는 방법의 수
# 퀸은 위아래, 대각선으로 움직일 수 있다. 
n = int(input())
str_row = [0] * n # 직선상의 개수
right_row  = [0] * (2 * n - 1) # 오른쪽 대각선의 개수
left_row = [0] * (2 * n - 1) # 왼쪽 대각선의 개수


result = 0
def queen(idx):
    global result
    if idx == n:
        result += 1
        return
    for i in range(n):
        if str_row[i] + left_row[idx + i] + right_row[idx - i] == 0:
            str_row[i] = left_row[idx + i] = right_row[idx - i] = 1
            queen(idx + 1)
            str_row[i] = left_row[idx + i] = right_row[idx - i] = 0

queen(0)
print(result)