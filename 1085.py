x, y, w, h = map(int, input().split())

num = []

num.append(x)
num.append(y)
num.append(w-x)
num.append(h-y)

print(min(num))