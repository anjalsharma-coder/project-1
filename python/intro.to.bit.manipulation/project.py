# ================================
# MY SECRET CODE BIT SCANNER
# ================================
# Topics:
# Bits and Binary | AND and OR | NOT and XOR
# Left Shift and Right Shift | Odd or Even with XOR | Counting Bits

secret_code = 89
access_key = 21



print("================================")
print("MY SECRET CODE BIT SCANNER")
print("================================")
print("Secret Code:", secret_code, "Binary:", (secret_code))
print("Access Key:", access_key, "Binary:", (access_key))

print("============================================")

print("Binary numbers use only 0 and 1.")
print("Secret Code Binary:", secret_code)
print("Access Key Binary:", access_key)


print("=======================================================")
# PART 2 - AND and OR
andresult = secret_code & access_key
orresult = secret_code | access_key

print("AND Result:", andresult, "Binary:", andresult)
print("OR Result:", orresult, "Binary:", orresult)
print("AND always prefer 0 where 0 is given.")
print("OR always prefers 1 where 1 is given.")


print("=======================================================")
notresult = (~secret_code) & 0b1111
xorresult = secret_code ^ access_key

print("NOT Secret Code within 4 bits:", notresult, "Binary:", notresult)
print("NOT flips the number.")
print("XOR Result:", xorresult, "Binary:", xorresult)
print("XOR gives 1 when the compared bits are different(0,1).")


print("=======================================================")

left_shift = secret_code << 1
right_shift = secret_code >> 1

print("Left Shift Result:", left_shift, "Binary:", (left_shift, 5))
print("Right Shift Result:", right_shift, "Binary:", (right_shift))
print("Left shift moves bits left. Right shift moves bits right.")


print("=======================================================")
# PART 5 - ODD OR EVEN WITH XOR
xor_check = secret_code ^ 1

print("Secret Code XOR 1:", xor_check)

if xor_check == secret_code - 1:
    print("Secret Code is Odd because XOR with 1 reduced it by 1.")
else:
    print("Secret Code is Even because XOR with 1 increased it by 1.")


print("=======================================================")
bit_count = secret_code.bit_count()

print("Number of 1 bits in Secret Code:", bit_count)
