def isBalance(p):
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                return False
    else:
        return True # P가 이미 올바른 괄호 문자열일때
    
def div(p):
    open_p = 0
    close_p = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
            
        if open_p == close_p:
            return p[:i + 1], p[i + 1:]
    
def solution(p):
    if p == '':
        return ''
    
    u, v = div(p)
    
    if isBalance(u):
        return u + solution(v)
    
    answer = '('
    
    answer += solution(v)
    
    answer += ')'
    
    for k in u[1:len(u) - 1]:
        if k == '(':
            answer += ')'
        else:
            answer += '('
    
    return answer