def bisection_root(x):
    epsilon = 0.000001
    num_guesses = 0
    low = 0.0
    high = x
    guess = (high + low) / 2

    while abs(guess**2 - x) >= epsilon:
        print(f"low = {low}  high = {high}  guess = {guess}")
        
        if guess**2 < x:
            low = guess
        else:
            high = guess
        
        guess = (high + low) / 2
        print(f"error = {guess**2 - x}")
        num_guesses += 1

    if abs(guess**2 - x) <= epsilon:
        print(f"Square root of {x} is approximately {guess}")
        print(f"num_guesses = {num_guesses}")
    return guess
bisection_root(25)