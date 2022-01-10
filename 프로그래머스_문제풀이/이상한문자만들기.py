def solution(s):
    s = s.split(" ")
    result = []
    for words in s:
        answer = ''
        for i in range(len(words)):
            if i % 2 == 0:
                answer += words[i].upper()
            else:
                answer += words[i].lower()
                
        result.append(answer)
    
    return ' '.join(result)