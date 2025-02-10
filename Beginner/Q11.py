inp=int(input("Enter number: ")) 

while inp>=10:
    inp=sum(int(i) for i in str(inp))

print(inp)
