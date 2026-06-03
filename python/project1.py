#Types of DATA
passenger_name = "Aarav" #string value
destination = "Goa"  #string value
ticket_price = 850.50            #float value
number_of_tickets = 3        # int
is_available = True      #boolean value

print("Passenger's name", passenger_name)
print("What is the destination?", destination)
print("What is the price?", ticket_price)
print("How many tickets are available?", number_of_tickets)
print("Is it available", is_available)

print("The type of the text")
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))


#arithmetic
total = ticket_price * number_of_tickets
print("The total price of three tickets is: $", total )

#Comparison 
print("Is the price more than $500?", ticket_price > 500)
print("More than 2 in stock?", number_of_tickets > 2)
print("Is the price exactly $850.50?", ticket_price == 850.50)


#string 
a = "Travel ticket price"
b = " to goa"
c = a+b
print(c)

#Swapping values
morningticket  = 700
eveningticket = 900
print("Price Before:", morningticket ,"and", eveningticket)

temp = morningticket
pricea = eveningticket
priceb = temp
 
print("Price After:", morningticket ,"and", eveningticket)