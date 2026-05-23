# ==========================================
# 1 Number Guess Analysis
# ==========================================

greater_than_50 = 0

less_or_equal_50 = 0

for count in range(5):

    number = int(input("Enter number: "))

    if number > 50:

        greater_than_50 += 1

    else:

        less_or_equal_50 += 1

print("Numbers greater than 50:", greater_than_50)

print("Numbers less than or equal to 50:", less_or_equal_50)
# ------------------------------------------

# ==========================================
# 2 Check Armstrong Number
# ==========================================

number = int(input("Enter a 3-digit number: "))

original = number

total = 0

while number > 0:

    digit = number % 10

    total += digit ** 3

    number = number // 10

if total == original:

    print("Armstrong number")

else:

    print("Not an Armstrong number")
# ------------------------------------------

# ==========================================
# 3 Reverse a Number Using Loop
# ==========================================

number = int(input("Enter a number: "))

reverse = 0

while number > 0:

    digit = number % 10

    reverse = reverse * 10 + digit

    number = number // 10

print("Reversed number:", reverse)
# ------------------------------------------

# ==========================================
# 4 FizzBuzz
# ==========================================

for number in range(1, 31):

    if number % 3 == 0 and number % 5 == 0:

        print("FizzBuzz")

    elif number % 3 == 0:

        print("Fizz")

    elif number % 5 == 0:

        print("Buzz")

    else:

        print(number)
# ------------------------------------------

# ==========================================
# 5 Password Strength Check
# ==========================================

password = input("Enter password: ")

has_digit = False

has_vowel = False

has_uppercase = False

for character in password:

    if character.isdigit():

        has_digit = True

    if character.lower() in "aeiou":

        has_vowel = True

    if character.isupper():

        has_uppercase = True

if has_digit and has_vowel and has_uppercase:

    print("Strong password")

else:

    print("Weak password")

# ==========================================
# FINAL LEARNING
# ==========================================

# Concepts covered:
# = loops
# = nested conditions
# = counters
# = string traversal
# = mathematical logic
# = prime numbers
# = Armstrong numbers
# = reversing numbers
# = boolean flags
# = input validation

# ==========================================