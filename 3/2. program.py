sub1=int(input("Enter first subject's marks: "))
sub2=int(input("Enter second subject's marks: "))
sub3=int(input("Enter third subject's marks: "))
sub4=int(input("Enter fourth subject's marks: "))

avg=(sub1+sub2+sub3+sub4)/4
print(avg)

if(avg>=90):
    print("Grade: A  Pass")
elif(avg>=80 and avg<90):
    print("Grade: B Pass")
elif(avg>=70 and avg<80):
    print("Grade: C Pass")
elif(avg>=60 and avg<70):
    print("Grade: D Pass")
else:
    print("Grade: F fail")
