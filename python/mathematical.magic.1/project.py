print("Hello user")

print("====================================")
n = input("Enter What are binary numbers")
print("====================================")

print("A binary number is expressed in the base-2 system, which uses only two digits: 0 and 1")

print("Computers use binary numbers because their physical hardware is built using transistors that operate as simple on/off electronic switches, 1 is on whereas 0 is off")

n = input("Now enter a binary number(Remember it onl contains number 1 and 0): ")

decimal = 0 
hello = len(n)- 1 

for digit in n: 
    value = int(digit) * (2 ** hello)
    decimal += value
    hello = hello - 1 

print("This is the decimal for your binary number: ",decimal)

