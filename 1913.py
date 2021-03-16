n = int(input())
target = int(input())

res = [[0] * n for _ in range(n)]
a, b = 0, 0 # target 의 좌표를 구하기 위한 변수 선언
num = n * n # (0,0)의 위치는 무조건 n * n이 온다.
x, y = -1, 0 


for i in range(2*n-1): # 방향을 전환하는 횟수는 2*n-1로 항상 일정함
    for j in range((2*n-i)//2): # 방향을 전환하고 몇번 이동해야하는지를 정함. 
                                # n이 5일 경우 5, 4, 4, 3, 3, 2, 2, 1, 1을 움직이며 
                                # 처음에만 n만큼 그 다음부터는 n-1만큼 2번 움직임.
        if i % 4 == 0: # Down
            x += 1
            
        elif i % 4 == 1: # Right
            y += 1
            
        elif i % 4 == 2: # Up
            x -= 1
            
        else: # Left
            y -= 1
            

        res[x][y] = num
        num -= 1

        if (num + 1) == target:
            a, b = x, y

for i in res:
    print(*i)

print(a+1, b+1)
