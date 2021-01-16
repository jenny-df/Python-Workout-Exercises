#1
# from random import *
# def guessing_game():
# 	correct = randint(0,100)
# 	guesses = 0
# 	print("\nWelcome to Jennifer's number-guessing game!\n\n A number between 0 and 100 will randomly be generated and you have to guess what it is in less than 6 guesses otherwise you lose!")
# 	while guesses < 6:
# 		guess = input("\nGuess a number!\n")
# 		try:
# 			guess = int(guess)
# 			if guess >=0 and guess <= 100: 
# 				if guess == correct:
# 					print("You have guessed the correct number!!!\n\n The number was "+str(correct) +" and you guessed it in "+str(guesses+1)+" tries")
# 					break
# 				elif guess< correct:
# 					print("The number you guessed is too low")
# 					guesses+=1
# 				elif guess > correct:
# 					print("The number you guessed is too high")
# 					guesses+=1
# 			else:
# 				print("Please enter a number between 0 and 100")
# 		except:
# 			print("Please enter a number")

# guessing_game()
# Initialize the zero-valued list with 100 length
zeros_list = [0] * 100 

# Declare the zero-valued tuple with 100 length
zeros_tuple = (0,) * 100  

# Extending the "vector_list" by 3 times
vector_list = [[1, 2, 3]]
for i, vector in enumerate(vector_list * 3):  
	print([(i + 1) * e for e in vector])
	print("{0} scalar product of vector: {1}".format((i + 1), [(i + 1) * e for e in vector]))
