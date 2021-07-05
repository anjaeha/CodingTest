
t = int(input())

for case in range(t):
    q = input()
    arr_len = int(input())

    if arr_len == 0:
        input_arr = input()
        input_arr = []
    else:
        input_arr = list(map(int, input()[1:-1].split(',')))

    is_re = False
    is_ok = True
    front = 0
    back = 0

    for act in q:
        try:
            if act == 'R':
                is_re = not is_re
            elif act == 'D' and not is_re:
                front += 1
            elif act == 'D' and is_re:
                back += 1
        except:
            is_ok = False
            print('error')
            break

    
    if is_ok:
        if front + back <= arr_len:
            if not is_re:
                input_arr = input_arr[front:arr_len - back]
                print(str(input_arr).replace(' ',''))
            else:
                input_arr = input_arr[::-1][back:arr_len - front]
                print(str(input_arr).replace(' ',''))
        else:
            print('error')