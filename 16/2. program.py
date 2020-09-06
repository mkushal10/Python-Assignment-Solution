num=65
for row in range(5):
    for col in range(0,row+1):
        ch=chr(num)
        print(ch,end="")

        num=num+1 
    print()
