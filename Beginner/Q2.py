inp=input("enter string: ")

alpha=0
digit=0
for i in range(len(inp)):
    if inp[i].isalpha():
        alpha+=1
    elif inp[i].isdigit():
        digit+=1

print(f"Alphabets: {alpha} & Number: {digit}")