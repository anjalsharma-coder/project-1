x = "Welcome to our website."
z = "This website will help you change your mood and make you feel better"
print (x)
print (z)
name = input("Please enter your name: ")
print ("HI!",name)
mood_rate = int(input("Rate your mood out of 10 from 1 to 10!!: "))
if mood_rate == 5:
      print("Having a neutral mood is not bad but make sure you take your time and talk to your to your close ones about it.")
elif mood_rate < 5:
	print("We hope you are aware that having a bad mood can affect your health and can cause an irritated mind.We will make sure to help you in the best way possible. Participate in the activity below")
else:
	print("Superb, we are happy that you are feeling good today, participate in the activity below to look at the note we provided you")
mood = input("How is your mood today?  (Warning: Use capital letter for the first letter of the word.)Type one of these: Cheerful, Excited, Relaxed, Optimistic, Pessimistic, Sad, Boring, Guilty, Irritated, Neutral: ")
if mood == "Cheerful":
    print("We are happy to know that you are in a good mood")
elif mood == "Excited":
    print("Seems something really exciting is coming into your life, always be like this. ")
elif mood == "Relaxed":
    print("Great! We are glad that you are feeling relaxed today.")
elif mood == "Optimistic":
    print("That's amazing! Fun fact: Your positive energy can brighten not only your day but also of people around you")
elif mood == "Pessimistic":
    print("Drink water! Take a short break and give yourself some time!")
elif mood == "Sad":
    print("It's ok to have sad days make sure to give yourself some time! and it's ok to take breaks!")
elif mood == "Boring":
    print("We hope this website helps brighten your mood!")
elif mood == "Guilty":
    print("Every moood is okay take care of yourself today!")
elif mood == "Irritated":
    print("You may be having a bad day but this doesn't reflect you/")
elif mood == "Neutral":
    print("Sometimes this is the best mood to have!")
else: 
    print ("ERROR! You haven't typed in any mood from the given options.Please try again.")

