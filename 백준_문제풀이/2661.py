n = int(input())

def check(num):
    for i in range(1, len(num) // 2 + 1):
        if num[-i:] == num[-(i*2): -i]:
            return False
    else:
        return True


def answer(num):
    global n
    if len(num) == n:
        print(num)
        exit()

    for i in '123':
        if check(num + str(i)):
            answer(num + str(i))
    return

answer('1')