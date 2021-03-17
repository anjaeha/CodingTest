N = int(input())

def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return lst[0] * 5000 + 50000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]: return lst[1] * 1000 + 10000
        return 2000 + (lst[1] + lst[2]) * 500
    for i in range(3):
        #같은 눈이 2개만 나오는 경우 찾기 위함
        if lst[i] == lst[i+1]: return 1000 + lst[i] * 100
    return lst[-1] * 100

print(max(money() for i in range(N)))

# set은 중복을 제거한 집합