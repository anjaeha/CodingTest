def solution(n, t, m, p): # 말해야하는 숫자 T개, 게임의 참가하는 인원M, 순서 P
    answer = ''
    word = '0'
    
    def change(num, idx): # 진수, 숫자
        temp = ''
        while idx > 0:
            if idx % num >= 10:
                temp += chr(idx % num + 55)
            else:
                temp += str(idx % num)
            idx //= num

        return temp[::-1]

    for i in range(1, 30000):
        word += change(n, i)
    
    for i in range(t):
        answer += word[(p - 1) + (m * i)]
        
    return answer