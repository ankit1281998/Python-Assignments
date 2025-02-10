list=[1,2,3,4,5]
index=10

try:
    print(list[index])
except IndexError:
    print("Index out of range")