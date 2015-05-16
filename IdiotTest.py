#Idiot Test Game

print("Welcome to the Idiot Test! This game will test your wit and determine whether or not you are an idiot. So let's get started!")
name = input("What's you name?")

done = False
score = 0

while not done:
	choice = input("Press 'x' to begin...")
	if choice == "x":
	
		print()

	choice = input("Q1: Do they have a 4th of July in England? Type 'yes' or 'no'...")
	if choice == "yes":
		score += 5
		print("Correct!")
	elif choice:
		print("Incorrect!")
	
	print()

	choice = input("Q2: Is it legal for a man in California to marry his widow's sister? Type 'yes' or 'no'...")
	if choice == "no":
		score += 5
		print("Correct!")
	else:
		print("Incorrect!")
	
	print()

	choice = input("Q3: Some months have 31 days. How many have 28 days?   ")
	if choice == "12" or choice == "twelve":
		score += 5
		print("Correct!")
	else:
		print("Incorrect!")
	
	print()

	choice = input("""Q4: A man builds a house rectangular in shape. All sides have a southern exposure. A bear walks by. What color is the bear? 
					a: brown
					b: white
					c: black
					d: red ...""")
	if choice == "b":
		score += 5
		print("Correct!")
	else:
		print("Incorrect!")
	
	print()

	choice = input("Q5: A clerk in the butcher shop is 5 foot 10 inches tall. What does he weigh?   ")
	if choice == "meat":
		score += 5
		print("Correct!")
	else:
		print("Incorrect!")
	
	print()
	
	choice = input("Q6: Your father has 3 children: Snap, Crackle, and ______ ?   ")
	if choice == name or choice == "me":
		score += 5
		print("Correct!")
		done = True
	else:
		print("Incorrect!")
		done = True

	print()

if done:
	print("Congratulations! You've made it to the end of the test! Your score was", score, ".")
	if score < 15:
		print("Good job! You failed you are a total idiot! Time to celebrate!")
	elif score == 15 or score == 20:
		print("Decent job! You are not an idiot nor a genius...you are normal")
	else:
		print("All hail", name, "!", "You are a genius!")

choice = input("press 'q' to quit, press 's' to see solutions")
if choice == 's':
	print(""" Solutions:
	q1: Everywhere has a 4th of July and a 2nd and 3rd etc.
	q2: A man cannot have a widow if he is still alive...
	q3: Every month has at least 28 days.
	q4:	The house would have to be at the North Pole, and therefore the bear is a Polar Bear
	q5: They weigh meat at a butcher shop
	q6: He is your father and therefore are the missing name...""")
elif choice == 'q':
	done = False
else:
	print("invalid input")


