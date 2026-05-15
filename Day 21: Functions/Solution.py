# ==========================================
# PYTHON FUNCTIONS – SOLUTIONS
# ==========================================

# ------------------------------------------

# 1️⃣Greet Students from List
def greet_students(names):
    for name in names:
        print("Hello", name, ", welcome to Python class.")

students = ["Rahul", "Anita", "Shubham"]
greet_students(students)

# ------------------------------------------

# 2️⃣Count Vowels in a String

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

result = count_vowels("Welcome to Python")
print("Total vowels:", result)

# ------------------------------------------

# 3️⃣Print Even Numbers from List
def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)
            
data = [1,2,3,4,5,6,7,8]
print_even_numbers(data)

# ------------------------------------------

# 4️⃣Print Student Marks from Dictionary

def student_marks(data):
    for subject in data:
        print(subject, ":", data[subject])
        
marks = {
"Maths":80,
"Science":75,
"English":90
}
student_marks(marks)

# ------------------------------------------

# 5️⃣Find Maximum from Tuple
def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

data = (5,10,2,18,7)
print("Maximum number:", find_max(data))

# ------------------------------------------

# 6️⃣Remove Duplicate Items using Set
def unique_items(items):
    unique = set(items)
    return unique

data = [1,2,3,2,4,1,5]
result = unique_items(data)
print(result)

# ------------------------------------------

# 7️⃣Read File with Exception Handling
def read_file(filename):
    try:
        file = open(filename,"r")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("File not found.")

read_file("data.txt")

# ------------------------------------------

# 8️⃣Write to File with Exception Handling
def write_file(filename, message):
    try:
        file = open(filename,"w")
        file.write(message)
        file.close()
        print("Message written successfully")
    except Exception as e:
        print("Error occurred:", e)

write_file("output.txt", "Welcome to Python")

# ------------------------------------------

# 9️⃣Divide Numbers with Exception Handling
def divide_numbers(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid value")

print(divide_numbers(10,2))
print(divide_numbers(10,0))

# ------------------------------------------

# 🔟Access List Element with Exception Handling
def access_list_element(data,index):
    try:
        return data[index]
    except IndexError:
        print("Index out of range")

numbers = [10,20,30,40]
print(access_list_element(numbers,2))
print(access_list_element(numbers,10))