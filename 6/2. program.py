num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

op=input("Please enter valid operator[+ - * / %]")

result=0

if op=="+":
    result=num1+num2
elif op=="-":
    result=num1-num2
elif op=="*":
    result=num1*num2
elif op=="/":
    result=num1/num2
elif op=="%":
    result=num1%num2
else:
    print("You entered invalid operator...")

print(num1,op,num2,"=",result)
