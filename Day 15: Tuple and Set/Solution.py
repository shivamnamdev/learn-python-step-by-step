# ==========================================
# TUPLE – SOLUTIONS
# ==========================================

# 1️⃣ Print Tuple Elements

students = ("Rahul","Aman","Neha","Priya")

print(students)
print(type(students))

# ------------------------------------------
# 2️⃣ Access First and Last Element

fruits = ("apple","banana","mango","grapes","orange")

print("First element:", fruits[0])
print("Last element:", fruits[-1])

# ------------------------------------------
# 3️⃣ Tuple Slicing

fruits = ("apple","banana","mango","grapes","orange")

print("First 3 fruits:", fruits[:3])
print("Last 2 fruits:", fruits[-2:])

# ------------------------------------------
# 4️⃣ Count Occurrence

nums = (1,2,3,2,4,2,5,2)

print("Count of 2:", nums.count(2))

# ------------------------------------------
# 5️⃣ Find Index

numbers = (10,20,30,40,50)

print("Index of 40:", numbers.index(40))

# ------------------------------------------
# 6️⃣ Loop Through Tuple

data = (5,10,15,20,25)

for value in data:
    print(value)

# ------------------------------------------
# 7️⃣ Print Tuple in One Line

nums = (1,2,3,4,5)

for value in nums:
    print(value, end=" ")

print()

# ------------------------------------------
# 8️⃣ Convert Tuple → List → Tuple

nums = (10,20,30)

temp = list(nums)

temp[2] = 40

nums = tuple(temp)

print(nums)

# ------------------------------------------
# 9️⃣ Check if Value Exists in Tuple

students = ("Pune","Delhi","Citadel","London")

if "London" in students:
    print("Found")
else:
    print("Not Found")

# ------------------------------------------
# 🔟 Count Total Students

class_for_python = (
    "Pallav","mahak","Yogesh","Amit","Sonal",
    "Abhay","Gungun","Akanksha","nishcal","Pradyumn"
)

print("Total students:", len(class_for_python))
# ------------------------------------------

# ==========================================
# SET – SOLUTIONS
# ==========================================

# ------------------------------------------
# 1️⃣ Create a Set


fruits = {"apple","banana","mango","orange"}

print(fruits)
print(type(fruits))

# ------------------------------------------
# 2️⃣ Observe Duplicate Removal

nums = {1,2,3,2,4,1,5}

print(nums)

# Sets automatically remove duplicates

# ------------------------------------------
# 3️⃣ Convert List → Set

numbers = [1,2,3,2,4,5,1,6]

result = set(numbers)

print(result)

# ------------------------------------------
# 4️⃣ Find Unique Values from List

students = ["Rahul","Aman","Rahul","Neha","Aman","Priya"]

unique_students = set(students)

print(unique_students)

# ------------------------------------------
# 5️⃣ Add Element to Set

fruits = {"apple","banana","mango"}

fruits.add("orange")

print(fruits)

# ------------------------------------------
# 6️⃣ Remove Element from Set

fruits = {"apple","banana","mango","orange"}

fruits.remove("banana")

print(fruits)

# ------------------------------------------
# 7️⃣ Loop Through Set

nums = {10,20,30,40}

for value in nums:
    print(value)

# ------------------------------------------
# 8️⃣ Check Membership

languages = {"python","java","c++","go"}

if "python" in languages:
    print("Python exists")
else:
    print("Python not found")

# ------------------------------------------
# 9️⃣ Find Common Elements (Intersection)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7}

print(set1.intersection(set2))

# ------------------------------------------
# 🔟 Find Unique Elements (Difference)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.difference(set2))

# ------------------------------------------
# 11 Combine Two Sets

set1 = {"apple","banana"}
set2 = {"mango","orange"}

result = set1.union(set2)

print(result)

# ------------------------------------------
# 12 Remove Duplicate Numbers from List

nums = [1,5,2,8,6,4,3,9,5,9,3,1]

unique_nums = list(set(nums))

print(unique_nums)

# ------------------------------------------
# 13 Unique Website Visitors

visitors = ["user1","user2","user3","user1","user2","user4"]

unique_visitors = set(visitors)

print("Total unique visitors:", len(unique_visitors))

# ==========================================
# KEY LEARNINGS
# ==========================================

# Tuple:
# - Ordered
# - Immutable
# - Allows duplicates

# Set:
# - Unordered
# - Mutable
# - Removes duplicates automatically

# Common set methods:
# add()
# remove()
# intersection()
# difference()
# union()

# Useful conversions:
# list()
# tuple()
# set()
# ==========================================