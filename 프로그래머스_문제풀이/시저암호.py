def solution(s, n):
    answer = ''
    for i in s:
        temp = ord(i)
        if i.isupper():
            temp = (temp - 65 + n) % 26
            answer += chr(temp + 65)
        elif i.islower():
            temp = (temp - 97 + n) % 26
            answer += chr(temp + 97)
        else:
            answer += i
    return answer