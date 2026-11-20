a = list(map(int, input("输入列表a:").split()))
b = list(map(int, input("输入列表b:").split()))
dict={}
s=min(len(a),len(b))
for i in range(s):
    dict[a[i]]=b[i]
print(dict)