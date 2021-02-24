
while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        l = []
        for i in range(n):
            l.append(int(input()))
        l.sort()
        i, j = 0, n-1
        flag = True
        while i < j:
            if l[i] + l[j] == x:
                print('yes %d %d' %(l[i], l[j]))
                flag = False
                break
            elif l[i] + l[j] < x:
                i += 1
            else:
                j -= 1
        if flag:
            print('danger')
    except:
        break