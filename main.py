'''
def finding_largest():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    largest = a 
    if b > largest:
        largest = b 
    if c > largest:
        largest = c 
    return largest

print(finding_largest())
'''

#CHATGPT bana verdiği task:
def finding_square_cube_double():
    nummer = float(input("Sayı gir köpke"))
    sqr = nummer**2
    cube = nummer**3
    double = nummer*2
    return sqr , cube, double
print(finding_square_cube_double())
