n = 20


input("Formula Method: one calculation.")
steps = 1
print("steps=", steps, "O(1)")

input("Loop Method: per step depending on the item")
steps = 0
for i in range(n):
    steps = steps + 1 # +=1
print("steps=", steps, "O(n)")


input("Double Loop Method: double step depending on the item")
steps = 0
for i in range(n):
    for j in range(n):
        steps = steps + 1 # +=1
print("steps=", steps, "O(n*n)")

input(" Big Omega = best case")
input(" Big theta = average case")
input(" Big O = worst case")

