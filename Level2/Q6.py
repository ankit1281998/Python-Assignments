num=int(input("enter number: "))

i=0
flag=0
while 2**i<=num:
    if 2**i==num:
        flag=1
        print("Yes")
        break
    i+=1   
if flag==0: 
    print("No")         