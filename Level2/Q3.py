from collections import defaultdict
arr = [1, 2, 3, 4, 5]
k = 6
ans=0
hm=defaultdict(int)
for i in arr:
    if k-i in hm:
        print(hm[k-i],k,i)
        ans+=(hm[k-i])
    

    hm[i]+=1
    print(hm)

print(ans)
