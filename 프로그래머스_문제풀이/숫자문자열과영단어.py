def solution(s):
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(10):
        if word[i] in s:
            s = s.replace(word[i], str(i))
    
    return int(s)