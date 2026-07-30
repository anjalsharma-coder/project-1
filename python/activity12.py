file = open("activity12.txt", "a")
file.write("/nThis paragraph tells you about coding/n")
file.write("Thankyou")

file.close()

file = open("activity12.txt","r")

print(file.read())

file.close()