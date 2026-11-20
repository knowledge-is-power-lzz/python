s=list(map(int,input().split()))
current=1
for i in range(len(s)):
    current*=s[i]
print(current)