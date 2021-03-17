import math

for i in range(int(input())):
    N, M = map(int, input().split())

    a = math.factorial(M)
    b = math.factorial(M-N)
    c = math.factorial(N)
    print(a//b//c)


#   경우의 수를 구하는 문제로 M개 중에 N개를 고르는 문제  => mCn
#   M! // M-N! // N! 로 해결.