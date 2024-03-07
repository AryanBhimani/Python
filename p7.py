list = [1,2,3,4,5,6,7,8,9]
min = list[0]
max = list[0]
for I in list:
    if I>max:
        max = I
    elif I<min:
        min = I
print("Maximum number is ", max)
print("Minimum number is ", min)