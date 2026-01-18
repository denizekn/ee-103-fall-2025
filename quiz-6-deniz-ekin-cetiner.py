class Student:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
my_student = Student("Deniz")
my_student.say_hello()