a = int(input("enter your first choice  :"))
b = int(input("enter your second choice :"))
c = int(input("enter your third choice :"))

if(a>=b and a>=c):
    print("first number is largest",a)
elif(b>=c and b>=a):
    print("second number is largest",b)
elif(c>=a and c>=b):
    print("third is largest",c)