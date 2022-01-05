def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for a in range(len(nums)):
        for b in range(a + 1, len(nums)):
            for c in range(b + 1, len(nums)):
                if prime_number(nums[a] + nums[b] + nums[c]):
                    answer += 1
    return answer