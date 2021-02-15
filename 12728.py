import math

T = int(input())

for i in range(T):
    n = int(input())

    num = int((3 + math.sqrt(5))**n)

    if num >= 100:
        num = str(num)
        a = num[-1:-4:-1][::-1]
    else:
        num = str(num)
        a = num.zfill(3)

    print("Case #%d: %s" %(i+1, a))

#런타임에러 ㅠ
#수학적으로 풀어야하는듯?