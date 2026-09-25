quizscore = [11,98,100,56,74,89,56,43,39]

print("Quiz Scores")

print("Quiz_scores:", quizscore)

print("=============================")
print("Direct Access")
firstscore = quizscore[0]

print("First student score:", firstscore)
print("Time complexity: O(1)")
print("Omega notation: Best Case")
print("Takes only one step")



targetscore = 39 
steps = 0 
found = False

for score in quizscore:
    steps += 1
    if score == targetscore:
        found = True
        print("=============================")
        print("Loop")
        print("Target score found:", score)

if found == False:
       print("This score is not found in the list")

print("This is a loop, so the time complexity is O(n)")
print("Theta notation: Average Case")

pairsteps = 0
for score1 in quizscore:
     for score2 in quizscore:
        pairsteps += 1

print("=============================")
print("Nested Loop")
print("Total pairsteps:", pairsteps)
print("It is a nested loop, so the time complexity is O(n*n), it compares each score with every single score in the list")
print("Big O notation: Worst Case")


print("=============================")
print("Case Comparison")
print("Best Case: O(1) - Takes only one step")  
print("Average Case: O(n) - Takes n steps, n is the number of scores in the list")
print("Worst Case: O(n*n) - Takes n*n steps(double the steps of the input)")