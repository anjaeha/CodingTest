def check(temp):
    return temp == temp[::-1]

def solution(s):
    MAX = -1
    length = len(s)
    
    for i in range(length):
        for j in range(i, length+1):
            if check(s[i:j]):
                if MAX < len(s[i:j]):
                    MAX = len(s[i:j])
    return MAX


print(solution("abcdcba"))