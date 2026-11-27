import random
current=random.randint(1, 100)
low,high=1,100

while True:
    s=input(f"请猜一个{low}-{high}的整数:")
    if not s.isdecimal() or int(s) <= 0:
        print("输入无效！请输入大于 0 的纯数字（不能包含字母、符号或空格）。")
        continue
    n=int(s)
    if n < low or n > high:
        print(f"超出范围！请输入 {low}-{high} 之间的整数。")
        continue
    if n>current:
        print("大了")
        high = min(high, n - 1) 
    elif n<current:
        print("小了")
        low = max(low, n + 1) 
    else:
        print("恭喜你，猜对了！")   
        break