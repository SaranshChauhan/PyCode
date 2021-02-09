import os
os.system("clear")

# Multiple Classes]

class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] #blank list

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        val = 0
        for student in self.students:
            val += student.get_grade()

        return val / len(self.students)

s1 = Student("Cook",17,91)
s2 = Student("Raiz",19,88)
s3 = Student("Kiran",18,87)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.get_average_grade())