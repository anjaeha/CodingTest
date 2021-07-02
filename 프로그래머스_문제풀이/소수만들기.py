from itertools import combinations

def check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(nums):
    result = 0
    combination = list(combinations(nums, 3))
    
    for combi in combination:
        if check(sum(combi)):
            result += 1
        
    return result