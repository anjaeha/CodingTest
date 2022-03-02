a, b = map(int, input().split())

count = 1
while 1:
    if a == b:
        break
    count += 1
    if b % 10 == 1:
        b //= 10
    else:
        if b % 2 == 0:
            b //= 2
        else:
            count = -1
            break
    if b < a:
        count = -1
        break

print(count)