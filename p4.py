def f(s):
    return s ==s[:: -1]
A = str(input("Enter string :"))
ans =  f(A)
if ans:
    print("Palindrome")
else:
    print("not Palindrome") 