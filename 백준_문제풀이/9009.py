t = int(input())

s = [0, 1]

for i in range(2, 50):
    s.append(s[i-1] + s[i-2])

for case in range(t):
    n = int(input())


    array = []

    while n:
        for i in range(50):
            if s[i] <= n:
                t = s[i]

        n -= t
        array.append(t)

            
    array.sort()

    print(*array)