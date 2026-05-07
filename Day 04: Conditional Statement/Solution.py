# ==========================================
# IF-ELSE Assignment Solutions
# ==========================================

# 1. Positive Number Check
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")

# ------------------------------------------

# 2. Voting Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")

# ------------------------------------------

# 3. Check if number is exactly equal to 10
num = int(input("Enter a number: "))

if num == 10:
    print("Number is exactly 10")

# ------------------------------------------

# 4. Even or Odd Number
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ------------------------------------------

# 5. Compare Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First is greater")
else:
    print("Second is greater or equal")

# ------------------------------------------

# 6. Pass or Fail
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# ------------------------------------------

# 7. Working Age Check
age = int(input("Enter age: "))

if age >= 18 and age <= 60:
    print("Working age")
else:
    print("Not working age")

# ------------------------------------------

# 8. Valid or Invalid Number
num = int(input("Enter a number: "))

if num < 0 or num > 100:
    print("Invalid number")
else:
    print("Valid number")

# ------------------------------------------

# 9. Empty Input Check
value = input("Enter a value: ")

if value:
    print("Input received")
else:
    print("No input given")

# ------------------------------------------

# 10. Vowel Check
ch = input("Enter a character: ")

if ch in "aeiou":
    print("Vowel")
else:
    print("Not a vowel")

# ------------------------------------------

# 11. Python Related Word Check
word = input("Enter a word: ")

if "py" in word:
    print("Python related")
else:
    print("Not Python related")

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