inp=int(input("Enter a number: "))
ans=0
for i in range(1,inp):
    if inp%i==0:
        ans+=i

if ans==inp:
    print("Yes")
else:
    print("No") 