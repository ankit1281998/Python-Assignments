number_list = [7, 2, 5, 1, 9, 3]

l=len(number_list)
number_list.sort()

if l%2==0:
    print((number_list[l//2-1]+number_list[l//2])/2)
else:
    print(number_list[l//2])