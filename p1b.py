x = int(input("Enter First Site :"))
y = int(input("Enter First Site :"))
z = int(input("Enter First Site :"))
s = (x+y+z)/2
print(s) 
area = float (s*(s-x)*(s-y)*(s-z))**0.5 
print ("area of triangle is %0.2f"  %area) 