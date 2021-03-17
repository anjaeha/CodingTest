wh = [0 for i in range(101)]
wh[1] = wh[2] = wh[3] = 1

for i in range(0, 98):
    wh[i + 3] = wh[i] + wh[i+1]


for case in range(int(input())):
    N = int(input())
    print(wh[N])