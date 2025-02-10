start=int(input("Enter the start number: "))
end=int(input("Enter the end number: "))
sum=0

for i in range(start,end):
    if i%2!=0:
        sum+=i
print("Sum of odd  numbers:", sum)