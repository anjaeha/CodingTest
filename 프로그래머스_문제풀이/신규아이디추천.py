# 아이디의 길이는 3자 이상 15자 이하
# 알파벳 소문자, 숫자, 빼기, 언더바, 마침표만 사용 가능
# 마침표는 처음과 끝에 사용X, 연속X

def solution(new_id):
    
    # 1단계 소문자로 치환
    new_id = new_id.lower()

    newId = ''
    # 2단계 허용된 문자 제외하고 제거
    for i in new_id:
        if i.isalnum():
            newId += i
        elif i in ['-', '_', '.']:
            newId += i
        else:
            continue
    
    new_id = ''
    temp = ''
    # 3단계 마침표가 2번 이상이면 하나로 치환
    for i in range(len(newId)):
        if newId[i] != '.':
            if temp:
                new_id += '.'
                temp = ''
            new_id += newId[i]          
        else:
            temp += '.'
            
    # 4단계 아이디의 처음에 위치한 마침표 제거
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    # 5단계 빈 문자열이라면 a추가
    else:
        new_id += 'a'
    
    # 6단계 길이가 16자 이상이면, 15자로
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
    
    # 7단계 길이가 2 이하라면 3이 될때까지 마지막 문자를 반복
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id