from itertools import permutations

def check(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    set_val = set()
    for i in range(len(numbers), 0, -1):
        for val in list(map("".join, permutations(numbers, i))):
            if check(int(val)):
                set_val.add(int(val))

    return len(set_val)


print(solution("17"))