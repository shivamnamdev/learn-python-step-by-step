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