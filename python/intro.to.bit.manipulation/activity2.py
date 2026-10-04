n = int(input("Enter a number: "))
binary = input("Left shift. Guess: " + str(n) + "<<1 = ? ")

input("NOT - it filps the number. Press Enter now ")
print(" 89 =", bin(12)[2:])
print(" NOT 89 =", ~89)

input("XOR - different bits(0,1) gives 1 and same bits (0,0)(1,1) gives 0. Press Enter ")
print(" 12 ^ 10 =", 12 ^ 10)

input("Left shift - multiples by 2. Press Enter ")
print(n, "<<1 =", n << 1, " your guess: ", binary)

input("Right shift - divides by 2. Press Enter ")
print(n, ">> 1 =", n >> 1)