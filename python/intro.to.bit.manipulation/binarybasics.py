n = int(input("Enter a number:"))
binary = input("Guess its binary number:")

input("Binary. Press Enter ")
print(" decimal", n, "-> binary", bin(n)[2:])
print(" your guess:", binary)

input("And - both bits must be 1. Press Enter")
print(" 79 =", bin(79)[2:] )
print(" 90 =", bin(90)[2:] )
print(" 79 & 90 =", 79 & 90 )

input("OR - at least one bit must be 1. Press Enter")
print("79 | 90 =", 79 | 90)