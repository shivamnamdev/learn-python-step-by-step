# ==========================================
# DICTIONARY – SOLUTIONS
# ==========================================

# ==========================================
# 🟢 Level 1 — Basic Dictionary Understanding
# ==========================================

# ------------------------------------------
# 1️⃣ Create a dictionary for a car

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "color": "Black"
}

print(car)

print(car["brand"])

print(car["year"])

# ------------------------------------------
# 2️⃣ Update dictionary value

person = {
    "name":"Rahul",
    "age":25,
    "city":"Pune"
}

person["city"] = "Mumbai"

person["profession"] = "Engineer"

print(person)

# ------------------------------------------
# 3️⃣ Delete values

data = {
    "a":10,
    "b":20,
    "c":30
}

del data["b"]

print(data)

# ------------------------------------------

# ==========================================
# 🟡 Level 2 — keys(), values(), items()
# ==========================================

# ------------------------------------------
# 4️⃣ Print all keys

student = {
    "name":"Priya",
    "age":21,
    "course":"Python"
}

for key in student.keys():

    print(key)

# ------------------------------------------
# 5️⃣ Print all values

for value in student.values():

    print(value)

# ------------------------------------------
# 6️⃣ Print both key and value

for key, value in student.items():

    print(key, value)

# ------------------------------------------

# ==========================================
# 🟠 Level 3 — Logic Building
# ==========================================

# ------------------------------------------
# 7️⃣ Count total subjects

marks = {
    "science":18,
    "maths":20,
    "english":15,
    "history":17
}

print("Total subjects:", len(marks))

# ------------------------------------------
# 8️⃣ Find subject with highest marks

highest_subject = ""
highest_marks = 0

for subject, marks_value in marks.items():

    if marks_value > highest_marks:

        highest_marks = marks_value
        highest_subject = subject

print(highest_subject)

# ------------------------------------------
# 9️⃣ Print subjects with marks greater than 17

for subject, marks_value in marks.items():

    if marks_value > 17:

        print(subject)

# ------------------------------------------

# ==========================================
# 🔵 Level 4 — Nested Dictionary
# ==========================================

# ------------------------------------------
# 🔟 Total marks per subject

students_marks = {
    "science": {"internals": 75,"externals":10},
    "maths": {"internals": 65,"externals":11}
}

for subject, data in students_marks.items():

    total = data["internals"] + data["externals"]

    print(subject, total)

# ------------------------------------------
# 1️⃣1️⃣ Find subject with highest total marks

highest_subject = ""
highest_total = 0

for subject, data in students_marks.items():

    total = data["internals"] + data["externals"]

    if total > highest_total:

        highest_total = total
        highest_subject = subject

print(highest_subject)

# ------------------------------------------
# 1️⃣2️⃣ Safe access using .get()

print(
    students_marks["science"].get("internals")
)

print(
    students_marks["science"].get(
        "practicals",
        "Key not found"
    )
)

# ------------------------------------------

# ==========================================
# 🔥 Bonus Thinking Question
# ==========================================

# ------------------------------------------
# 1️⃣3️⃣ Count subjects without len()

marks = {
    "science":18,
    "maths":20,
    "english":15,
    "history":17
}

count = 0

for key in marks:

    count += 1

print("Total subjects:", count)

# ==========================================
# KEY LEARNINGS
# ==========================================

# Dictionary:
# stores data in key:value pair

# Access value:
# dict[key]

# Update value:
# dict[key] = value

# Add new key:
# dict[new_key] = value

# Delete key:
# del dict[key]

# keys()
# returns all keys

# values()
# returns all values

# items()
# returns key-value pair

# get()
# safely accesses keys

# Nested Dictionary:
# dictionary inside dictionary

# Dictionary improves:
# - structured data handling
# - fast lookup
# - real-world data modeling
# ==========================================