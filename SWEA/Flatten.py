T = 10

for tc in range(1, T + 1):
    n = int(input())
    box = list(map(int, input().split()))

    for i in range(n):
        MAX = max(box)
        MIN = min(box)

        box[box.index(MAX)] -= 1
        box[box.index(MIN)] += 1
    
    print("#%d %d" %(tc, max(box) - min(box)))