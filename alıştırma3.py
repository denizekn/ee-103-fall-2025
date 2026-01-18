number = int(input("Bir sayı girin: "))

while number < 1000:
    if number % 2 == 0:
        print(number)
    number = number - 1
    if number == -1:
        print("Sayı sıfıra ulaştı.")
        break