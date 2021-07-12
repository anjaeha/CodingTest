def solution(s):
    for i in range(10):
        if 'zero' in s:
            s = s.replace('zero', '0')
        elif 'one' in s:
            s = s.replace('one', '1')
        elif 'two' in s:
            s = s.replace('two', '2')
        elif 'three' in s:
            s = s.replace('three', '3')
        elif 'four' in s:
            s = s.replace('four', '4')
        elif 'five' in s:
            s = s.replace('five', '5')
        elif 'six' in s:
            s = s.replace('six', '6')
        elif 'seven' in s:
            s = s.replace('seven', '7')
        elif 'eight' in s:
            s = s.replace('eight', '8')
        elif 'nine' in s:
            s = s.replace('nine', '9')
            
    return int(s)