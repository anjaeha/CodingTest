from collections import Counter

n = int(input())
n_list = sorted(list(map(int, input().split())))

m = int(input())
m_list = list(map(int, input().split()))

n_list = Counter(n_list)

for i in m_list:
    print(n_list[i], end = ' ')