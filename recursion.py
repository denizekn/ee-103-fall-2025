def reverse_str(s):
    if s == "" :
        return ""
    return s[-1] + reverse_str(s[:-1])
s = str(input("Enter a string to reverse: "))
print(f"Reversed string of {s} is: ", reverse_str(s)) 