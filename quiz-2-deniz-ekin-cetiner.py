input_number = input("Enter an integer value with 5 digits: ")
digit_sum = 0

for i in input_number:
    digit_sum += int(i)

print(f"The sum of the digits is {digit_sum}")

if digit_sum % 2 == 0:
    print("The sum of the digits is even.")
else:
    print("The sum of the digits is odd.")
       
                