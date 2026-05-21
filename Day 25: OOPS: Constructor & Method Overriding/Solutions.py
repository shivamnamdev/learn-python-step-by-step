# ==========================================
# OOP ASSIGNMENT – SOLUTIONS
# Constructor + Polymorphism + Overriding
# ==========================================

# ==========================================
# Program 1:
# Constructor Behavior & Default Values
# ==========================================

class student_database:

    name = "Unknown"

    course = "Python"

    def __init__(self, named="newname", courses="newcourses"):

        self.name = named

        self.course = courses


student1 = student_database("Rahul", "Java")

student2 = student_database("Aman", "C++")

student3 = student_database("Priya", "Data Science")

student4 = student_database()


print(student1.name, student1.course)

print(student2.name, student2.course)

print(student3.name, student3.course)

print(student4.name, student4.course)

# Output:
# Rahul Java
# Aman C++
# Priya Data Science
# newname newcourses

# Explanation:
# 4th object used default values

# It did not fail because
# constructor parameters already
# contain default values
# ------------------------------------------

# ==========================================
# Program 2:
# Instance vs Class Variable
# ==========================================

class student_database:

    name = "Unknown"

    course = "Python"

    def __init__(self, named="newname", courses="newcourses"):

        self.name = named

        self.course = courses


student1 = student_database("Rahul", "Java")

student2 = student_database("Aman", "C++")

student3 = student_database()


print(student1.name)

print(student_database.name)


student_database.course = "Data Science"


print(student1.course)

print(student2.course)

print(student3.course)

# Output:
# Rahul
# Unknown

# Java
# C++
# newcourses

# Explanation:
# No object updated

# Because all objects already have
# instance variable "course"

# Instance variable gets priority
# over class variable
# ------------------------------------------

# ==========================================
# Program 3:
# Polymorphism Using Loop
# ==========================================

class Student:

    def show(self):

        print("I am a student")


class Teacher:

    def show(self):

        print("I am a teacher")


class Admin:

    def show(self):

        print("I manage the system")


objects = [
    Student(),
    Teacher(),
    Admin()
]

for obj in objects:
    obj.show()

# Output:
# I am a student
# I am a teacher
# I manage the system

# Explanation:
# Same method name behaves differently

# This is polymorphism

# If one class does not have show()
# then program gives:
# AttributeError
# ------------------------------------------

# ==========================================
# Program 4:
# Method Overriding Behavior
# ==========================================

class Math:

    def add(self, a, b):

        print(a + b)

    def add(self, a, b, c, d):

        print(a + b + c + d)


m = Math()

m.add(2,3)

# Output:
# TypeError

# Explanation:
# First method got replaced
# by second method

# Python does not support
# traditional method overloading

# Only latest method survives
# ------------------------------------------

# ==========================================
# Program 5:
# Method Overloading (Python Way)
# ==========================================

class Math2:

    def add(self, a, b, c=0):

        print(a + b + c)

    def multiply(self, *numbers):

        print(sum(numbers))


a = Math2()

a.add(2, 3)

a.add(2, 3, 4)

# Output:
# 5
# 9


m = Math2()

m.multiply(2, 3)

m.multiply(2, 3, 4, 5)

# Output:
# 5
# 14

# Explanation:
# add() works with different inputs
# because c has default value

# *numbers accepts multiple values

# This creates flexible functions
# ------------------------------------------

# ==========================================
# FINAL CONCEPT QUESTIONS
# ==========================================

# 1. Why is __init__ preferred?

# __init__ runs automatically
# during object creation

# No need to call method manually

# Helps initialize object properly

# ==========================================

# 2. Class Variable

# Shared among all objects

# Stored inside class

# ==========================================

# 3. Instance Variable

# Separate copy for every object

# Stored inside object

# ==========================================

# 4. Why Python does NOT support
# traditional overloading?

# Python replaces old method
# with latest method

# Same method name cannot exist
# multiple times traditionally

# ==========================================

# 5. Key idea behind polymorphism

# Same method name
# different behavior

# Example:
# show() behaves differently
# for Student, Teacher, Admin

# ==========================================

# 6. What happens when two methods
# have same name in same class?

# Latest method overrides old method

# Previous method gets removed

# ==========================================
# FINAL LEARNINGS
# ==========================================

# __init__()
# constructor method

# Polymorphism:
# one method
# multiple behaviors

# Overriding:
# latest method replaces previous one

# *args:
# accepts multiple positional arguments

# Default parameter:
# provides optional values

# OOP helps in:
# = reusability
# = flexibility
# = real-world modeling
# ==========================================