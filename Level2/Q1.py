l1 = [1, 2, 3, 4, 5] 
l2 = [4, 5, 6, 7, 8]

s=set(l1)
ans=[]
for i in l2:
    if i in s:
        ans.append(i)
print(ans)
