number = input("Enter a number: ")
your_name = input("Enter your name: ")

even = 0
for i in number:
    i = int(i)
    if i % 2 == 0:
        even += i

print(f"Sum of even digits: {even}")

last_digit = even % 10
print(f"Last digit of the sum is: {last_digit}")

for _ in range(last_digit):
    print(your_name)