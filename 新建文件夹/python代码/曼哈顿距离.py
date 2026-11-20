a = list(map(int, input("输入点a(2个整数,空格分隔):").split()))
b = list(map(int, input("输入点b(2个整数,空格分隔):").split()))

distance = abs(a[0] - b[0]) + abs(a[1] - b[1])

print("曼哈顿距离：", distance)