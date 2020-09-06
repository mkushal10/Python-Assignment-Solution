print("What you want to find from following:")
print("Press 1 for  area of  circle")
print("Press 2 for area of rectangle")
print("Press 3 for circumference of circle")
print("Press 4 for area of a square")

op=int(input("Enter number 1 2 3 4:"))

if op==1:
    radius=float(input("Enter radius of circle:"))
    print("Area of circle is,",(22/7)*radius**2)

elif op==2:
    length=float(input("Enter length of reactangle:"))
    breadth=float(input("Enter breadth of rectangle:"))
    print("Area of rectangle is",length*breadth)

elif op==3:
    radius=float(input("Enter radius of circle:"))
    print("circumference of circle is,",2*(22/7)*radius)

elif op==4:
    side=float(input("Enter side of square:"))
    print("Area of square is",side*side)

else:
    print("You have been selected wrong character")
