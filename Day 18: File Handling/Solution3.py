# ==========================================
# PYTHON FILE HANDLING – ADVANCED SOLUTIONS
# ==========================================


# Q1. Count number of lines in a file

file = open("sample.txt", "w")

file.write("Python\n")
file.write("Java\n")
file.write("C++\n")

file.close()

file = open("sample.txt", "r")

lines = file.readlines()

print("Total lines:", len(lines))

file.close()

# ------------------------------------------
# Q2. Count total number of characters

file = open("sample.txt", "r")

content = file.read()

print("Total characters:", len(content))

file.close()

# ------------------------------------------
# Q3. Print each line with line number

file = open("sample.txt", "r")

line_number = 1

for line in file:

    print(line_number, ":", line.strip())

    line_number += 1

file.close()

# ------------------------------------------
# Q4. Write numbers 1 to 20 and print even

file = open("numbers.txt", "w")

for num in range(1, 21):

    file.write(str(num) + "\n")

file.close()

file = open("numbers.txt", "r")

for line in file:

    number = int(line.strip())

    if number % 2 == 0:
        print(number)

file.close()

# ------------------------------------------
# Q5. Find student with highest marks


file = open("marks.txt", "w")

file.write("Rahul 78\n")
file.write("Shivam 92\n")
file.write("Aman 85\n")

file.close()

file = open("marks.txt", "r")

highest_marks = 0
topper = ""

for line in file:

    data = line.split()

    name = data[0]
    marks = int(data[1])

    if marks > highest_marks:
        highest_marks = marks
        topper = name

print("Topper:", topper)
print("Highest Marks:", highest_marks)

file.close()

# ------------------------------------------
# Q6. Demonstrate tell()

file = open("sample.txt", "r")

print("Initial cursor position:", file.tell())

file.read(5)

print("Cursor position after reading:", file.tell())

file.close()

# ------------------------------------------
# Q7. Demonstrate seek()

file = open("sample.txt", "r")

print(file.read(5))

file.seek(0)

print(file.read())

file.close()

# ------------------------------------------
# Q8. Copy contents of one file to another

source = open("sample.txt", "r")

content = source.read()

source.close()

destination = open("copy.txt", "w")

destination.write(content)

destination.close()

print("File copied successfully")

# ------------------------------------------
# Q9. Count specific word occurrence

file = open("sample.txt", "r")

content = file.read()

word = "Python"

count = content.count(word)

print(word, "appears", count, "times")

file.close()

# ------------------------------------------
# Q10. Remove blank lines from file

file = open("dirty.txt", "w")

file.write("Python\n")
file.write("\n")
file.write("Java\n")
file.write("\n")
file.write("C++\n")

file.close()

file = open("dirty.txt", "r")

clean = open("clean.txt", "w")

for line in file:

    if line.strip() != "":
        clean.write(line)

file.close()
clean.close()

print("Blank lines removed successfully")

# ==========================================
# KEY LEARNINGS
# ==========================================

# read()       --> reads full content
# readline()   --> reads one line
# readlines()  --> returns list of lines

# tell() --> gives current cursor position

# seek(0) --> moves cursor to beginning

# strip() --> removes spaces/newline

# split() --> splits string into list

# count() --> counts occurrences

# File handling modes:
# 'r' --> read
# 'w' --> write
# 'a' --> append

# Always close files after use
# ==========================================