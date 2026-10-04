number = int(input("Type you number: "))

digit = len(str(number))# to calc the number of digits in the number 

resultnumber = 0 

temp = number 
while temp > 0:
    hello = temp % 10 
    resultnumber += hello ** digit
    temp //=10


if number == resultnumber:
    print(number ," is an Armstrong number")
else:
    print(number ," is not an Armstong number ")