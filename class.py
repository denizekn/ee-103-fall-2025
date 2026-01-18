class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        return f""" 
        Name: {self.name} 
        Grades: {self.grades} 
        Average: {self.average():.2f}
        """

s1 = Student("Deniz")
s2 = Student("Ekin")
s3 = Student("Duygu")
s1.add_grade("Math", 85)
s1.add_grade("Physics", 90)
s1.add_grade("Chemlab", 90)
s2.add_grade("Math", 70)
s2.add_grade("Physics", 75)
s2.add_grade("Chemlab",70)
s3.add_grade("Math",31)
s3.add_grade("Physics", 31)
s3.add_grade("Chemlab", 31)
print(s1)
print(s2)
print(s3)