from math import gcd
int1=int(input("Enter the first number: "))
int2=int(input("Enter the second number: "))

lcm=abs(int1*int2)//gcd(int1,int2)

print("LCM of",int1,"and",int2,"is",lcm)