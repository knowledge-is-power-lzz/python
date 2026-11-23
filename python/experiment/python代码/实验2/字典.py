from collections import defaultdict

s=input()
max_val=float('-inf')
cnt=defaultdict(int)
for st in s:
    cnt[st]+=1
for i,x in cnt.items():
    if x>max_val:
        max_val=x
        ans=i

print(ans)
print(max_val)
print(dict(cnt)) 