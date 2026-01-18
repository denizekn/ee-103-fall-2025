def create_student(name, age):
    return (name, age)
def describe_student(student_tuple):
    name, age = student_tuple
    return f"Student {name} is {age} years old."

if __name__ == "__main__":
    student_name = input("Enter student name: ")
    student_age = int(input("Enter student age: "))

    student = create_student(student_name, student_age)
    student_description = describe_student(student)
    print(student_description)