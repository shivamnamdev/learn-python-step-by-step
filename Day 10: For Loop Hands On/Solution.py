# ==========================================
# Python Loop Practice – Solutions
# ==========================================

# ==========================================
# 1️⃣ Count Even and Odd Numbers
# ==========================================

even_count = 0

odd_count = 0

for count in range(10):

    number = int(input("Enter number: "))

    if number % 2 == 0:

        even_count += 1

    else:

        odd_count += 1

print("Total even numbers:", even_count)

print("Total odd numbers:", odd_count)

# ------------------------------------------

# ==========================================
# 2️⃣ Sum of Only Positive Numbers
# ==========================================

total = 0

for count in range(7):

    number = int(input("Enter number: "))

    if number > 0:

        total += number

print("Sum of positive numbers:", total)
# ------------------------------------------

# ==========================================
# 3️⃣ Find Largest Number (Without max())
# ==========================================

largest = None

for count in range(5):

    number = int(input("Enter number: "))

    if largest is None or number > largest:

        largest = number

print("Largest number:", largest)
# ------------------------------------------

# ==========================================
# 4️⃣ Count Vowels and Consonants
# ==========================================

word = input("Enter a word: ")

vowels = 0

consonants = 0

for character in word.lower():

    if character.isalpha():

        if character in "aeiou":

            vowels += 1

        else:

            consonants += 1

print("Total vowels:", vowels)

print("Total consonants:", consonants)
# ------------------------------------------

# ==========================================
# 5️⃣ Print Prime Numbers from 1 to N
# ==========================================

n = int(input("Enter value of N: "))

for number in range(2, n + 1):

    is_prime = True

    for value in range(2, number):

        if number % value == 0:

            is_prime = False

            break

    if is_prime:

        print(number)
# ------------------------------------------

# ==========================================
# 6️⃣ Number Guess Analysis
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
# 7️⃣ Check Armstrong Number
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
# 8️⃣ Reverse a Number Using Loop
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
# 9️⃣ FizzBuzz
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
# 🔟 Password Strength Check
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