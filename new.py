print(" Welcome to the Number Guessing Game!")
import random
random_number = random.randint(0, 100)
user_guess = input("Guess a number between 0 - 100: ")
user_guess = int(user_guess)
if  user_guess == random_number:
    print("You guessed it right ")
elif user_guess > random_number:
    print("You guessed it wrong! Try a smaller number")
elif user_guess < random_number:
    print("You guessed it wrong! Try a larger number")  
print(f"The random number was: {random_number}")