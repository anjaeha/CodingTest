for case in range(int(input())):
    x, y = map(int, input().split())
    dis = y - x
    count = 0
    move = 1
    move_plus = 0
    
    while move_plus < dis:
        count += 1
        move_plus += move

        if count % 2 == 0:
            move += 1
    
    print(count)