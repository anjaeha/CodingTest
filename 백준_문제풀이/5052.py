t = int(input())

for tc in range(t):
    n = int(input())
    numbers = [input() for _ in range(n)]

    numbers.sort()

    for i in range(n - 1):
        if numbers[i] == numbers[i + 1][:len(numbers[i])]:
            print('NO')
            break
    else:
        print('YES')