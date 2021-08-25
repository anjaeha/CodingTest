import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())

def solve(n):
    cnt = 0
    num = 1

    while 1:
        str_num = str(num)
        flag = True

        if len(str_num) == 1:
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i]) < int(str_num[i-1]):
                    continue
                else:
                    left = str_num[:i-1]
                    mid = str(int(str_num[i-1]) + 1)
                    right = '0' + str_num[i + 1:]
                    num = int(left + mid + right)
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:
                return num
            num += 1


if n >= 1023:
    print(-1)
elif n == 0:
    print(0)
else:
    print(solve(n))