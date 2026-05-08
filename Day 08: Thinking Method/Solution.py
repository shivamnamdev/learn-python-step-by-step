# ==========================================
# THE 4-STEP THINKING METHOD — PRACTICE SET
# ==========================================

# ==========================================
# STEP 1 — UNDERSTAND THE PROBLEM
# ==========================================

# ------------------------------------------
# Q1. Find Largest Number
# ------------------------------------------

# Problem:
# Find the largest value from the list

# Input:
# [4, 8, 2, 15, 6]

# Goal:
# Print the largest number

# ------------------------------------------
# Q2. Find Odd Numbers
# ------------------------------------------

# Problem:
# Find all odd numbers from list

# Input:
# [1,2,3,4,5,6,7,8]

# Goal:
# Store and print odd numbers

# ------------------------------------------
# Q3. Count Vowels in String
# ------------------------------------------

# Problem:
# Count vowels from given string

# Input:
# "education"

# Goal:
# Print total vowel count

# ------------------------------------------
# Q4. Find Smallest Number
# ------------------------------------------

# Problem:
# Find smallest value from list

# Input:
# [12,5,8,2,15]

# Goal:
# Print smallest number

# ------------------------------------------
# Q5. Reverse a String
# ------------------------------------------

# Problem:
# Reverse the given string

# Input:
# "python"

# Goal:
# Print string in reverse order

# ==========================================
# STEP 2 — WRITE LOGIC IN HUMAN LANGUAGE
# ==========================================

# ------------------------------------------
# Q1. Find Largest Number
# ------------------------------------------

# Logic:
# 1. Assume first number is largest
# 2. Compare every number
# 3. If larger number found
#    update largest
# 4. Print largest number

# ------------------------------------------
# Q2. Find Odd Numbers
# ------------------------------------------

# Logic:
# 1. Take one number from list
# 2. Check if number not divisible by 2
# 3. If yes, store it
# 4. Print stored odd numbers

# ------------------------------------------
# Q3. Count Vowels in String
# ------------------------------------------

# Logic:
# 1. Take one character from string
# 2. Check if character is vowel
# 3. If yes, increase count
# 4. Print total count

# ------------------------------------------
# Q4. Find Smallest Number
# ------------------------------------------

# Logic:
# 1. Assume first number is smallest
# 2. Compare all numbers
# 3. If smaller number found
#    update smallest
# 4. Print smallest number

# ------------------------------------------
# Q5. Reverse a String
# ------------------------------------------

# Logic:
# 1. Start from last character
# 2. Move backward one by one
# 3. Print each character
# 4. Reverse string gets formed

# ==========================================
# STEP 3 — CONVERT TO ALGORITHM / STEPS
# ==========================================

# ------------------------------------------
# Q1. Find Largest Number
# ------------------------------------------

# Step 1:
# Store first value as largest

# Step 2:
# Loop through list

# Step 3:
# Compare each value

# Step 4:
# Update largest if bigger value found

# ------------------------------------------
# Q2. Find Odd Numbers
# ------------------------------------------

# Step 1:
# Create empty odd list

# Step 2:
# Loop through numbers

# Step 3:
# Check odd condition

# Step 4:
# Store odd numbers

# ------------------------------------------
# Q3. Count Vowels in String
# ------------------------------------------

# Step 1:
# Create vowel counter

# Step 2:
# Loop through string

# Step 3:
# Check vowel condition

# Step 4:
# Increase count

# ------------------------------------------
# Q4. Find Smallest Number
# ------------------------------------------

# Step 1:
# Assume first value as smallest

# Step 2:
# Loop through list

# Step 3:
# Compare each value

# Step 4:
# Update smallest

# ------------------------------------------
# Q5. Reverse a String
# ------------------------------------------

# Step 1:
# Start index from last position

# Step 2:
# Loop backward

# Step 3:
# Print characters one by one

# Step 4:
# Decrease index

# ==========================================
# STEP 4 — WRITE PYTHON CODE
# ==========================================

# ------------------------------------------
# Q1. Find Largest Number
# ------------------------------------------

numbers = [4, 8, 2, 15, 6]

largest = numbers[0]

for value in numbers:

    if value > largest:
        largest = value

print("Largest number:", largest)

# ------------------------------------------
# Q2. Find Odd Numbers
# ------------------------------------------

numbers = [1,2,3,4,5,6,7,8]

odd_numbers = []

for value in numbers:

    if value % 2 != 0:
        odd_numbers.append(value)

print("Odd numbers:", odd_numbers)

# ------------------------------------------
# Q3. Count Vowels in String
# ------------------------------------------

text = "education"

count = 0

for ch in text:

    if ch in "aeiou":
        count += 1

print("Total vowels:", count)

# ------------------------------------------
# Q4. Find Smallest Number
# ------------------------------------------

numbers = [12,5,8,2,15]

smallest = numbers[0]

for value in numbers:

    if value < smallest:
        smallest = value

print("Smallest number:", smallest)

# ------------------------------------------
# Q5. Reverse a String
# ------------------------------------------

text = "python"

index = len(text) - 1

while index >= 0:

    print(text[index], end="")

    index -= 1

# ==========================================
# FINAL LEARNING
# ==========================================

# Never directly jump into coding.
#
# First:
# Understand the problem
#
# Then:
# Write logic in simple English
#
# Then:
# Convert logic into algorithm steps
#
# Finally:
# Write Python code
#
# This technique improves:
# - problem solving
# - interview thinking
# - coding confidence
# ==========================================