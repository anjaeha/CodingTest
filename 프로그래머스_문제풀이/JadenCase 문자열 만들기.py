def solution(s):
    s = s.split(' ')
    answer = []
    for word in s:
        if word and word[0].isalpha():
            temp = word[0].upper() + word[1:].lower()
            answer.append(temp)
        else:
            answer.append(word.lower())
    
    return ' '.join(answer)