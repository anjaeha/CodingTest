def clock(arr):
    newarr = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            newarr[i][j] = arr[2 - j][i]
    return newarr

def anticlock(arr):
    newarr = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            newarr[i][j] = arr[j][2 - i]
    return newarr

def move(c):
    global cube
    if c == 'U+':
        cube[4][0], cube[3][0], cube[5][0], cube[2][0] = cube[2][0], cube[4][0], cube[3][0], cube[5][0]
        cube[0] = clock(cube[0])
        return
    elif c == 'U-':
        cube[4][0], cube[2][0], cube[5][0], cube[3][0] = cube[3][0], cube[4][0], cube[2][0], cube[5][0]
        cube[0] = anticlock(cube[0])
        return
    elif c == 'D+':
        cube[2][2], cube[4][2], cube[3][2], cube[5][2] = cube[4][2], cube[3][2], cube[5][2], cube[2][2]
        cube[1] = clock(cube[1])
        return
    elif c == 'D-':
        cube[2][2], cube[5][2], cube[3][2], cube[4][2] = cube[5][2], cube[3][2], cube[4][2], cube[2][2]
        cube[1] = anticlock(cube[1])
        return
    elif c == 'F+':
        a, b, d = cube[4][0][2], cube[4][1][2], cube[4][2][2]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[1][0][0], cube[1][0][1], cube[1][0][2]
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        cube[5][2][0], cube[5][1][0], cube[5][0][0] = cube[0][2][2], cube[0][2][1], cube[0][2][0]
        cube[0][2][2], cube[0][2][1], cube[0][2][0] = a, b, d
        cube[2] = clock(cube[2])
        return
    elif c == 'F-':
        a, b, d = cube[4][0][2], cube[4][1][2], cube[4][2][2]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[0][2][2], cube[0][2][1], cube[0][2][0]
        cube[0][2][2], cube[0][2][1], cube[0][2][0] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        cube[5][2][0], cube[5][1][0], cube[5][0][0] = cube[1][0][0], cube[1][0][1], cube[1][0][2]
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = a, b, d
        cube[2] = anticlock(cube[2])
        return
    elif c == 'B+':
        a, b, d = cube[4][0][0], cube[4][1][0], cube[4][2][0]
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[0][0][2], cube[0][0][1], cube[0][0][0]
        cube[0][0][2], cube[0][0][1], cube[0][0][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        cube[5][2][2], cube[5][1][2], cube[5][0][2] = cube[1][2][0], cube[1][2][1], cube[1][2][2]
        cube[1][2][0], cube[1][2][1], cube[1][2][2] = a, b, d
        cube[3] = clock(cube[3])
        return
    elif c == 'B-':
        a, b, d = cube[4][0][0], cube[4][1][0], cube[4][2][0]
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[1][2][0], cube[1][2][1], cube[1][2][2]
        cube[1][2][0], cube[1][2][1], cube[1][2][2] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        cube[5][2][2], cube[5][1][2], cube[5][0][2] = cube[0][0][2], cube[0][0][1], cube[0][0][0]
        cube[0][0][2], cube[0][0][1], cube[0][0][0] = a, b, d
        cube[3] = anticlock(cube[3])
        return
    elif c == 'L+':
        a, b, d = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
        cube[3][2][2], cube[3][1][2], cube[3][0][2] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = a, b, d
        cube[4] = clock(cube[4])
        return
    elif c == 'L-':
        a, b, d = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
        cube[3][2][2], cube[3][1][2], cube[3][0][2] = a, b, d
        cube[4] = anticlock(cube[4])
        return
    elif c == 'R+':
        a, b, d = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = a, b, d
        cube[5] = clock(cube[5])
        return
    elif c == 'R-':
        a, b, d = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = a, b, d
        cube[5] = anticlock(cube[5])
        return


t = int(input())
for case in range(t):
    cube = [[['w','w','w'],['w','w','w'],['w','w','w']],[['y','y','y'],['y','y','y'],['y','y','y']],[['r','r','r'],['r','r','r'],['r','r','r']],[['o','o','o'],['o','o','o'],['o','o','o']],[['g','g','g'],['g','g','g'],['g','g','g']],[['b','b','b'],['b','b','b'],['b','b','b']]] # 0위, 1아래, 2앞, 3뒤, 4왼, 5오 방향
    n = int(input())
    op = list(input().split())

    for i in op:
        move(i)

    for i in range(3):
        for j in range(3):
            print(cube[0][i][j], end = '')
        print()