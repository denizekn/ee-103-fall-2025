def approximate_method(x):
    epsilon = 0.0001
    step = 0.001
    guess = 0.0
    num_guesses = 0
    while True:
        if abs(guess**2 - x) < epsilon:
            break
        guess = guess + step
        num_guesses = num_guesses + 1
    print(f"Square root of {x} is {guess}")
approximate_method(25)