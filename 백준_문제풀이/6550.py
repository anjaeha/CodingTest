import sys
input = sys.stdin.readline


while True:
    line = input().strip()
    if not line:
        break

    s, t = line.split()
    cnt = 0
    flag = False
    for i in range(len(t)):
        if t[i] == s[cnt]:
            cnt += 1

        if cnt == len(s):
            flag = True
            break

    if flag == False:  
        print('No')
    else:
        print('Yes')