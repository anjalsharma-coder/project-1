familymembers = ["Angel", "Arnav", "Amit", "Charu", "Kirti"]
print("family members name:", familymembers)

#list
print("Total members: ", len(familymembers))
print("First member: ", familymembers[0])
print("Last student: ", familymembers[-1])
print("First three: ", familymembers[1:4])

familymembers.append("Pranav")
print(familymembers)
familymembers.remove("Arnav")
print("After removing Arnav: ", familymembers)
familymembers.sort()
print("Arranged alphabetically:", familymembers)
familymembers.reverse()
print("Reversed(descending):", familymembers)

#dictionary
friends = {"name": "Gunveen", "age": "17", "time:" "", }