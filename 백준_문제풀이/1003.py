import sys
input = sys.stdin.readline

zero = [1, 0, 1]
one = [0, 1, 1]


t = int(input())
for case in range(t):
    n = int(input())

    if len(zero) <= n:
        for i in range(len(zero), n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

    print(zero[n], one[n])