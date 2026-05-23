# ==========================================
# Python Assignment: For Loop Practice
# SOLUTIONS
# ==========================================
# ------------------------------------------

# ==========================================
# SECTION 1: Basic For Loop Programs
# ==========================================

# 1. Print numbers from 1 to 10

for number in range(1, 11):

    print(number)

# ------------------------------------------


# 2. Print numbers from 10 to 1

for number in range(10, 0, -1):

    print(number)

# ==========================================

# ------------------------------------------
# 3. Print your name 5 times

for count in range(5):

    print("Shivam")

# ==========================================

# ------------------------------------------
# 4. Print even numbers from 1 to 20

for number in range(1, 21):

    if number % 2 == 0:

        print(number)

# ==========================================

# ------------------------------------------
# 5. Print odd numbers from 1 to 20

for number in range(1, 21):

    if number % 2 != 0:

        print(number)
# ------------------------------------------

# ==========================================
# SECTION 2: Number-Based Logic Programs
# ==========================================

# ------------------------------------------
# 6. Print square of numbers from 1 to 10

for number in range(1, 11):

    print(number, "→", number ** 2)

# ==========================================

# ------------------------------------------
# 7. Print cube of numbers from 1 to 5

for number in range(1, 6):

    print(number, "→", number ** 3)

# ==========================================

# ------------------------------------------
# 8. Print multiplication table of 5

for number in range(1, 11):

    print(
        "5 ×",
        number,
        "=",
        5 * number
    )

# ==========================================

# ------------------------------------------
# 9. Print numbers divisible by 3
# between 1 and 30

for number in range(1, 31):

    if number % 3 == 0:

        print(number)

# ==========================================

# ------------------------------------------
# 10. Print sum of numbers from 1 to 10

total = 0

for number in range(1, 11):

    total += number

print("Total Sum:", total)
# ------------------------------------------

# ==========================================
# SECTION 3: String-Based Programs
# ==========================================

# ------------------------------------------
# 11. Print each character of a word

word = "Python"

for character in word:

    print(character)

# ==========================================

# ------------------------------------------
# 12. Count total characters in a word

word = "Programming"

count = 0

for character in word:

    count += 1

print("Total Characters:", count)

# ==========================================

# ------------------------------------------
# 13. Count vowels in a word

word = "Education"

vowel_count = 0

for character in word.lower():

    if character in "aeiou":

        vowel_count += 1

print("Total Vowels:", vowel_count)
# ------------------------------------------

# ==========================================
# SECTION 4: Basic Pattern Programs
# ==========================================

# ------------------------------------------
# 14. Print stars vertically

for star in range(5):

    print("*")

# ==========================================

# ------------------------------------------
# 15. Print 5 stars in one line

for star in range(5):

    print("*", end=" ")

# ==========================================
# FINAL LEARNING
# ==========================================

# Important concepts learned:
# = for loop
# = range()
# = conditions
# = even/odd checking
# = arithmetic operations
# = string traversal
# = counting logic
# = pattern printing

# ==========================================