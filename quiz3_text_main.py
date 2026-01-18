def sum_odd(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return n + sum_odd(n-1)
    return sum_odd(n-1)
print ("Sum of odd numbers from 1 to 10 is: ", sum_odd(10))