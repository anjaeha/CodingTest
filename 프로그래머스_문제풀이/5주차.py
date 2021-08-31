from itertools import product

def solution(word):
    answer = 0
    AEIOU = ['A', 'E', 'I', 'O', 'U']
    
    result = []
    for i in range(1, 6):
    	result += list(product(AEIOU, repeat = i))
        
    result.sort()
    
    for i in range(len(result)):
        result[i] = ''.join(result[i])
    
    answer = result.index(word) + 1
    
    return answer