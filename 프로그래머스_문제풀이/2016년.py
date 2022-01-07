def solution(a, b):
    answer = ''
    cal = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    count = 0
    for i in range(a):
        count += cal[i]
    count += b
    
    count %= 7
    return day[count - 1]