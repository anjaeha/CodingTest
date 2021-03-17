def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse=True)
    if sum(list(map(int, numbers))) == 0:
        numbers = list(set(numbers))
        
    return "".join(numbers)