arr = []

for i in range(9):
    arr.append(int(input()))

sum_s = sum(arr)
one = 0
two = 0

for i in range(8):
    for j in range(i+1, 9):
        if sum_s - (arr[i] + arr[j]) == 100:
            one = arr[i]
            two = arr[j]

arr.remove(one)
arr.remove(two)

arr.sort()

for i in arr:
    print(i)