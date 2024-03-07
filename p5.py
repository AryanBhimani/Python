A = int(input("Enter the number : "))
B = int(input("Enter the number : "))
print("value of a before swapping is ",A)
print("value of a before swapping is ",B)
def swap(A,B):
    temp = A;
    A = B;
    B = temp;
    print(temp)
    print("after swap value of a is ",A)
    print("after swap value of a is ",B)
swap(A,B)