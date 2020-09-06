a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

for i in range(1,a*b+1):
    if i%a==0 and i%b==0:
        print("LCM of number is",i)
        break

while a%b!=0:
    rem=a%b
    a=b
    b=rem
print("GCD of number is",b)
