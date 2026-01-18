x = 25
epsilon = 0.01
guess = 0.0
increment = 0.1

while abs(guess**2 - x) >= epsilon:
    guess += increment