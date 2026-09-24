n = 10

print("******************************")
print("RUNNING LAP TRACKER")
print("******************************")
print("Number of laps:", n)
print()


formula_total = n * (n + 1) // 2

print("Solution 1: Formula ")
print("Total Running Points:", formula_total)
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")
print()


# loop method
looptotal = 0
steps = 0
for lap in range(1, n + 1):
    looptotal = looptotal + lap
    steps = steps + 1

print("Solution 2: Loop Method")
print("Total Running Points:", looptotal)
print("Steps Taken:", steps)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print()


nestedtotal = 0
stepsnested = 0

for lap in range(1, n + 1):
    for point in range(1, lap + 1):
        nestedtotal = nestedtotal + 1
        stepsnested = stepsnested + 1

print("Solution 3: Nested Loop Method")
print("Total Running Points:", nestedtotal)
print("Steps Taken:", stepsnested)
print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
print()



print("ALGORITHM EFFICIENCY COMPARISON")

print("Formula Method: Fastest, uses only 1 calculation.")
print("Loop Method: Slower,repeats once for every lap.")
print("Nested Loop Method: Slowest, uses a loop inside another loop.")
print()
print("Best Method: Formula Method")
print("Reason: It has O(1) time complexity, so it stays fast even when laps increase.")
