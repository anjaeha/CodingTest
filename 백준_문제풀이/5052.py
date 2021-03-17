def check():
    for i in range(len(num) - 1):
        if num[i] == num[i+1][0:len(num[i])]:
            print('NO')
            return
    print('YES')

t = int(input())

for i in range(t):
    n = int(input())
    num = []
    for j in range(n):
        num.append(input())
    num.sort()
    check()    