def solution(numbers):
    answer = ''
    number = list(map(str, numbers))
    number.sort(key = lambda x : x * 3, reverse = True)
    
    return ''.join(number) if sum(numbers) != 0 else "0"