a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if a>=b and a>=c:
    print("a is largest: ",a)
elif b>=a and b>=c:
    print("b is largest: ",b)
else:
    print("c is largest: ",c)