first_name = "Denizr. " \
last_name = "Çetiner"

first_name_length = len(first_name)
last_name_length = len(last_name)

if first_name_length > last_name_length:
    print("First name is longer")
elif last_name_length > first_name_length:
    print("Last name is longer")
    print("Equal lengths")
