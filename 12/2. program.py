number = int(input(" Please Enter any Number: "))
summ = 0
for i in range(1, number):
    if(number % i == 0):
        summ = summ + i
if (summ == number):
    print(" %d is a Perfect Number" %number)
else:
    print(" %d is not a Perfect Number" %number)
