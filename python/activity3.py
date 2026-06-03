# if else elif statements
number =int(input("Enter the value: "))
if number > 0:
    print ("Your value is a positive number")
elif number == 0:
    print("Your value is neither a positive nor a negative number")
else:
    print ("Your value is a negative number")


#datetime module
import datetime
import calendar

date_timenow = datetime.datetime.now()
print("The time now",date_timenow)

print(calendar.calendar(2009))