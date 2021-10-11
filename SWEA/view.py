T = 10

for tc in range(1, T + 1):
    n = int(input())
    building = list(map(int, input().split()))
    result = 0
    for i in range(2, n - 2):
        left1 = building[i - 1]
        left2 = building[i - 2]
        right1 = building[i + 1]
        right2 = building[i + 2]
        MAX = max(left1, left2, right1, right2)
        temp = building[i] - MAX

        if temp > 0:
            result += temp
    
    print("#%d %d" %(tc, result))