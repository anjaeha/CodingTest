from itertools import product
def solution(word):
    words = []
    aeiou = ['A', 'E', 'I', 'O', 'U']

    for i in range(1, 6):
        temp = list(product(aeiou, repeat = i))
        for j in temp:
            words.append(''.join(j))
        
    words.sort()
    return words.index(word) + 1