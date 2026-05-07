# ==========================================
# IF-ELSE Assignment Solutions
# ========================================== 

# 1. Valid Digit Check
digit = input("Enter a digit: ")

if digit in "0123456789":
    print("Valid digit")
else:
    print("Invalid digit")

# ------------------------------------------

# 2. Boolean Variable Check
is_active = True

if is_active is True:
    print("System is active")

# ------------------------------------------

# 3. Adult or Minor
age = int(input("Enter age: "))

if (age > 18) is True:
    print("Adult")
else:
    print("Minor")

# ------------------------------------------

# 4. Identity Check
a = True
b = True

if a is b:
    print("Same identity")
else:
    print("Different identity")

# ------------------------------------------

# 5. Grade System
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# ------------------------------------------

# 6. Age Category
age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# ------------------------------------------

# 7. CHALLENGE Question
value = input("Enter something: ")

if value.isdigit():
    print("Number")
elif value in "aeiou":
    print("Vowel")
else:
    print("Consonant or string")

# ------------------------------------------

# Key Learnings:
# - if checks condition
# - else runs when condition is False
# - elif is used for multiple conditions
# - == compares values
# - is compares identity
# - % gives remainder
# - and/or/not are logical operators
# - input() always returns string