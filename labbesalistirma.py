# ------------------------------
# LABORATORY 5 - Python Practice
# ------------------------------

# ------------------------------
# TODO 1: Define a function to calculate the square of each number in a list
# ------------------------------
def square_list(numbers):
    squared = []
    for i in numbers:
        squared.append(i ** 2)
    return squared



# ------------------------------
# TODO 2: Create a list of numbers from 1 to 5
# ------------------------------
my_list = [1, 2, 3, 4, 5]
    # YOUR CODE HERE



# ------------------------------
# TODO 3: Call the function and print the result
# ------------------------------
print("Squared numbers:", square_list(my_list)) 
# Example output: Squared numbers: [1, 4, 9, 16, 25]


# ------------------------------
# TODO 4: Demonstrate a tuple (immutable structure)
# ------------------------------
my_tuple = (1, 2, 3, 4, 5)
print("my tuble is: ", my_tuple)
print("The second element of my tuble is: ", my_tuple[2])
    # YOUR CODE HERE


# YOUR CODE HERE to print the tuple and access elements


# ------------------------------
for d in range(1,11):
    for e in range(1,11):
        print(f"Answer = {d*e}")
    print("--------")
# ------------------------------
# YOUR CODE HERE


# ------------------------------
# TODO 6: Bonus - Combine list and loops to create a list of tuples
# ------------------------------
# Each tuple contains (number, its square)
combined_list = []
for i in range(1,5):
     combined_list.append((i,i**2,i**3))
    print(combined_list)

    # YOUR CODE HERE


# YOUR CODE HERE to print combined_list