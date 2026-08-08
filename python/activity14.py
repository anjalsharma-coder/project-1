with open("activity14.txt", "w") as file:
    file.write("This is the code for file handling part2")

with open("activity14.txt", "r") as file:

    second = file.readlines()

    for line in second:
        split = line.split()
        print(split)