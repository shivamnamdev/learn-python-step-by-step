# ==========================================
# OOP ASSIGNMENT – SOLUTIONS
# Understanding Class Variables
# and Instance Variables
# ==========================================

# ==========================================
# Reference Class
# ==========================================

class student_database:

    # Class Variables

    name = "Unknown"

    course = "Python"

    def add_student(self, named, courses):

        self.name = named

        self.course = courses

        print(self)

# ==========================================
# Program 1: Basic Object Behavior
# ==========================================

student1 = student_database()

student2 = student_database()

student3 = student_database()

student1.add_student("Rahul", "Java")

student2.add_student("Aman", "C++")

print(student1.name)
print(student1.course)

print(student2.name)
print(student2.course)

print(student3.name)
print(student3.course)

# Output:
# Rahul
# Java
# Aman
# C++
# Unknown
# Python

# Explanation:
# student3 did not get instance values
# so it used class variables

# ------------------------------------------

# ==========================================
# Program 2: Instance vs Class Variable
# ==========================================

student1 = student_database()

student1.add_student("Rahul", "Java")

print(student1.name)

print(student_database.name)

# Output:
# Rahul
# Unknown

# Explanation:
# student1.name became instance variable
# class variable remained unchanged

# self.name creates object-level variable

# ------------------------------------------

# ==========================================
# Program 3: Direct Update Without Method
# ==========================================

student2 = student_database()

student2.name = "New Value"

student2.course = "C++"

print(student2.name)
print(student2.course)

print(student_database.name)
print(student_database.course)

# Output:
# New Value
# C++
# Unknown
# Python

# Explanation:
# Direct assignment creates
# instance variables

# Class variables did not change

# ------------------------------------------

# ==========================================
# Program 4: Change Class Variable
# ==========================================

student1 = student_database()

student2 = student_database()

student3 = student_database()

student1.add_student("Rahul", "Java")

student_database.course = "Data Science"

print(student1.course)

print(student2.course)

print(student3.course)

# Output:
# Java
# Data Science
# Data Science

# Explanation:
# student1 already has instance variable
# so it did not use updated class variable

# student2 and student3
# still depend on class variable

# ------------------------------------------

# ==========================================
# Program 5: Add New Method
# ==========================================

class student_database:

    name = "Unknown"

    course = "Python"

    def add_student(self, named, courses):

        self.name = named

        self.course = courses

    def show_details(self):

        print("Name:", self.name)

        print("Course:", self.course)

        print()

# ------------------------------------------

student1 = student_database()

student2 = student_database()

student3 = student_database()

student1.add_student("Rahul", "Java")

student2.add_student("Aman", "C++")

student1.show_details()

student2.show_details()

student3.show_details()

# Output:
# Name: Rahul
# Course: Java

# Name: Aman
# Course: C++

# Name: Unknown
# Course: Python

# Explanation:
# Same method behaves differently
# because every object has different data

# self refers to current object

# ==========================================
# FINAL LEARNINGS
# ==========================================

# Class Variable:
# shared among all objects

# Instance Variable:
# unique for every object

# self.variable
# creates/accesses instance variable

# ClassName.variable
# accesses class variable

# Object checks:
# 1. instance variable first
# 2. then class variable

# Same method can behave differently
# depending on object data

# This concept is called:
# Object-Oriented Programming (OOP)

# OOP helps in:
# = code organization
# = reusability
# = real-world modeling
# ==========================================