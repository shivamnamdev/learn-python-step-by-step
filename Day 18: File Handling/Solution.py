# ==========================================
# PYTHON FILE HANDLING – SOLUTIONS
# ==========================================

# ------------------------------------------
# Q1. Create a file and write student names

file = open("students.txt", "w")

file.write("Rahul\n")
file.write("Shivam\n")
file.write("Aman\n")
file.write("Priya\n")
file.write("Neha\n")

file.close()

print("Student names written successfully")

# ------------------------------------------
# Q2. Read entire file content

file = open("students.txt", "r")

content = file.read()

print(content)

file.close()

# ------------------------------------------
# Q3. Append new student name

file = open("students.txt", "a")

file.write("Rohit\n")

file.close()

print("New student name appended successfully")

# ------------------------------------------
# Q4. Print only lines containing 'Python'

file = open("students.txt", "a")

file.write("Python Basics\n")
file.write("Java Programming\n")
file.write("Advanced Python\n")

file.close()

file = open("students.txt", "r")

for line in file:

    if "Python" in line:
        print(line)

file.close()

# ==========================================
# KEY LEARNINGS
# ==========================================

# 'w'  --> write mode
#         Creates new file
#         Removes old data

# 'r'  --> read mode
#         Reads file content

# 'a'  --> append mode
#         Adds new data
#         Keeps old data safe

# read() --> reads entire file

# for line in file:
# --> reads file line by line

# Always close files after use.
# ==========================================