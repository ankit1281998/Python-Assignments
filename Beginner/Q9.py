from collections import Counter
inp=input("Enter numbers: ") #write number with comma separated
lst=inp.split(",")
#print(lst)
print(Counter(lst))