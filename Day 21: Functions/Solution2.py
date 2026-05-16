# ==========================================
# PYTHON FUNCTIONS, *args, **kwargs,
# GLOBAL & LOCAL VARIABLES – SOLUTIONS
# ==========================================

# ------------------------------------------
# 1️⃣ Function Call Counter using Global Variable

count = 0

def show_count():

    global count

    count += 1

    print("Function called:", count, "times")

show_count()
show_count()
show_count()

# ------------------------------------------
# 2️⃣ sum_all(*args)

def sum_all(*args):

    total = 0

    for value in args:
        total += value

    return total

print(sum_all(10, 20, 30, 40))

# ------------------------------------------
# 3️⃣ print_all(*args)

def print_all(*args):

    for value in args:
        print(value)

print_all(10, "Python", [1,2,3])

# ------------------------------------------
# 4️⃣ combine_strings(*args)

def combine_strings(*args):

    sentence = ""

    for word in args:
        sentence += word + " "

    return sentence

print(combine_strings("Python", "is", "easy"))

# ------------------------------------------
# 5️⃣ student_details(**kwargs)

def student_details(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)

student_details(
    name="Shivam",
    age=25,
    course="Python"
)

# ------------------------------------------
# 6️⃣ filter_data(**kwargs)

def filter_data(**kwargs):

    for key, value in kwargs.items():

        if type(value) == int:
            print(key, ":", value)

filter_data(
    name="Rahul",
    age=22,
    marks=85,
    city="Delhi"
)

# ------------------------------------------
# 7️⃣ mixed_function(*args, **kwargs)

def mixed_function(*args, **kwargs):

    print("Positional Arguments:")

    for value in args:
        print(value)

    print("Keyword Arguments:")

    for key, value in kwargs.items():
        print(key, ":", value)

mixed_function(
    10,
    20,
    "Python",
    name="Shivam",
    city="Pune"
)

# ------------------------------------------
# 8️⃣ Pass List using *args

def print_values(*args):

    for value in args:
        print(value)

numbers = [10,20,30,40]

print_values(*numbers)

# ------------------------------------------
# 9️⃣ Pass Dictionary using **kwargs

def show_values(**kwargs):

    for value in kwargs.values():
        print(value)

student = {
    "name": "Aman",
    "age": 22,
    "course": "Python"
}

show_values(**student)

# ------------------------------------------
# 🔟 Area of Circle using Global Variable

pi = 3.14

def area_of_circle(radius):

    area = pi * radius * radius

    print("Area:", area)

area_of_circle(5)
area_of_circle(7)

# ------------------------------------------
# 1️⃣1️⃣ Find Maximum using *args

def find_max(*args):

    maximum = args[0]

    for value in args:

        if value > maximum:
            maximum = value

    return maximum

print(find_max(10, 50, 20, 90, 30))

# ------------------------------------------
# 1️⃣2️⃣ Count Total Keys using **kwargs

def count_keys(**kwargs):

    return len(kwargs)

print(count_keys(
    name="Rahul",
    age=22,
    city="Mumbai"
))

# ------------------------------------------
# 1️⃣3️⃣ Nested Loop using *args

def print_nested(*args):

    for group in args:

        for value in group:
            print(value)

print_nested(
    [1,2,3],
    ("Python", "Java"),
    [10,20]
)

# ------------------------------------------
# 1️⃣4️⃣ config(**kwargs) using get()

def config(**kwargs):

    print("Name:", kwargs.get("name", "Guest"))
    print("Theme:", kwargs.get("theme", "Light"))
    print("Language:", kwargs.get("language", "English"))

config(
    name="Shivam",
    theme="Dark"
)

# ------------------------------------------
# 1️⃣5️⃣ Unpacking using * and **

def student_info(name, age, city):

    print(name)
    print(age)
    print(city)

data_list = ["Rahul", 22, "Pune"]

student_info(*data_list)


def employee_info(name, salary):

    print(name)
    print(salary)

data_dict = {
    "name": "Aman",
    "salary": 50000
}

employee_info(**data_dict)

# ==========================================
# KEY LEARNINGS
# ==========================================

# Global Variable:
# declared outside function
# accessible inside function using global

# Local Variable:
# created inside function
# accessible only inside function

# *args
# accepts multiple positional arguments

# **kwargs
# accepts multiple keyword arguments

# args --> tuple
# kwargs --> dictionary

# .items()
# gives key-value pairs

# .values()
# gives only values

# get()
# safely accesses dictionary keys

# * --> unpack list/tuple
# ** --> unpack dictionary

# Functions improve:
# - code reuse
# - readability
# - modular programming
# ==========================================