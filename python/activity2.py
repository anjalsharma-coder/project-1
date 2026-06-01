#Types of DATA
snack_name = "Fries" #string value
price = 4             #integer(int)
quantity = 5.6         # float value
is_it_tasty = True      #boolean value

print("Snack's name", snack_name)
print("What is the price?", price)
print("How much quantity is in stock?", quantity)
print("Is it tasty", is_it_tasty)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_it_tasty))


#arithmetic
total = price * quantity
print("The total value is: $", total )
print("The sale price is: $", price - 0.85)
print("Double stock:", quantity * 2)

#Comparison 
print("Is the price more than 2?", price > 2)
print("More than 10 in stock?", quantity > 10)
print("Is the price exactly $4?", price == 4)

#string 
a = "Food shop"
b = " Open"
c = a+b
print(len(c),c)

#Swapping values
pricea = 5
priceb = 10
pricec = 15
print("Before:", pricea, pricec ,"and", priceb)

temp = pricea
pricea = priceb
priceb = pricec
pricec = temp
 
print("After:", pricea, pricec ,"and", priceb)