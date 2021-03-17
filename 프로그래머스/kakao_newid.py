# 2021 카카오 코딩테스트 신규아이디 추천 문제

def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    
    for word in new_id:
        if word.isalnum() or word in '-._':
            answer += word
            
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    else:
        answer
    
    if answer[-1] == '.':
        answer = answer[:-1]
    else:
        answer
        
    if answer == '':
        answer = 'a'
        
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:14]
        
    if len(answer) <= 2:
        answer = answer + answer[-1] * (3 - len(answer))
    return answer