# ==========================================
# WHILE LOOP ASSIGNMENT SOLUTIONS
# ==========================================
# ==========================================
# 🟢 Level 1: Understanding While Loop Structure
# ==========================================
# ------------------------------------------
# Q1. Print "Hello" 5 times using while loop
count = 0

while count < 5:
    print("Hello")
    count += 1

# ------------------------------------------

# Q2. Print numbers from 0 to 4
num = 0

while num < 5:
    print(num)
    num += 1

# ------------------------------------------

# Q3. Print numbers from 1 to 5
num = 1

while num <= 5:
    print(num)
    num += 1

# ------------------------------------------

# Q4. Print "Python" 3 times
count = 0

while count < 3:
    print("Python")
    count += 1

# ------------------------------------------

# Q5. Print even numbers from 0 to 10
num = 0

while num <= 10:
    print(num)
    num += 2
# ------------------------------------------
# ==========================================
# 🟡 Level 2: Understanding Condition & Truthy/Falsy
# ==========================================
# ------------------------------------------
# Q6.
# while -5:
#     print("Running")

# Explanation:
# -5 is a truthy value in Python.
# Since it never becomes False,
# loop runs infinitely.

# ------------------------------------------

# Q7.
flag = True
count = 0

while flag:
    print("Working")

    count += 1

    if count == 1:
        flag = False

# Output:
# Working

# ------------------------------------------

# Q8. Print "Loop Active" only once
flag = True

while flag:
    print("Loop Active")

    flag = False
# ------------------------------------------
# ==========================================
# 🟡 Level 3: Reverse & Counting Logic
# ==========================================
# ------------------------------------------
# Q9. Print numbers from 5 to 1
num = 5

while num >= 1:
    print(num)
    num -= 1

# ------------------------------------------

# Q10. Print numbers from 10 to 0
num = 10

while num >= 0:
    print(num)
    num -= 1

# ------------------------------------------

# Q11. Print numbers from 1 to 10 increasing by 2
num = 1

while num <= 10:
    print(num)
    num += 2
# ------------------------------------------
# ==========================================
# 🟡 Level 4: String Traversal Using While Loop
# ==========================================
# ------------------------------------------
# Q12. Print each character of "HELLO"
text = "HELLO"
index = 0

while index < len(text):
    print(text[index])
    index += 1

# ------------------------------------------

# Q13. Print characters of "python" separated by comma
text = "python"
index = 0

while index < len(text):
    print(text[index], end=",")

    index += 1

print()

# ------------------------------------------

# Q14. Print "abcde" in reverse order
text = "abcde"
index = len(text) - 1

while index >= 0:
    print(text[index])
    index -= 1

# ------------------------------------------

# Q15. Count characters without using len() directly
text = "Python"
index = 0
count = 0

while text[index:index+1] != "":
    count += 1
    index += 1

print("Total characters:", count)
# ------------------------------------------
# ==========================================
# 🟠 Level 5: Thinking Practice
# ==========================================
# ------------------------------------------
# Q16. Print numbers from 1 to 10 except 6
num = 1

while num <= 10:

    if num == 6:
        num += 1
        continue

    print(num)
    num += 1

# ------------------------------------------

# Q17. Print "Working" until count reaches 3
count = 0

while count < 3:
    print("Working")
    count += 1

# ------------------------------------------

# Q18. Print all characters with index number
text = "Python"
index = 0

while index < len(text):
    print(index, text[index])
    index += 1

# ------------------------------------------

# Q19. Print characters at even index positions
text = "Python"
index = 0

while index < len(text):

    if index % 2 == 0:
        print(text[index])

    index += 1

# ------------------------------------------

# Q20. Print "Loop Ended" after loop finishes
count = 0

while count < 3:
    print("Running")
    count += 1

print("Loop Ended")
# ------------------------------------------

# ==========================================
# WHILE LOOP + BREAK + CONTINUE SOLUTIONS
# ==========================================
# ------------------------------------------

# ==========================================
# Q1.
# Print numbers from 1 to 10
# Skip numbers 3 and 7 using continue
# ==========================================

num = 1

while num <= 10:

    if num == 3 or num == 7:
        num += 1
        continue

    print(num)

    num += 1

# ------------------------------------------

# ==========================================
# Q2.
# Print numbers from 1 onwards
# Stop loop when number becomes 6
# ==========================================

num = 1

while True:

    if num == 6:
        break

    print(num)

    num += 1

# ------------------------------------------

# ==========================================
# Q3.
# Print numbers from 1 to 15
# Skip all even numbers
# ==========================================

num = 1

while num <= 15:

    if num % 2 == 0:
        num += 1
        continue

    print(num)

    num += 1

# ------------------------------------------

# ==========================================
# Q4.
# Create a while True loop
# Break when number becomes greater than 5
# ==========================================

num = 1

while True:

    if num > 5:
        break

    print(num)

    num += 1

# ------------------------------------------

# ==========================================
# Q5.
# Print numbers from 1 to 10
# Skip numbers divisible by 4
# Stop when number becomes greater than 8
# ==========================================

num = 1

while num <= 10:

    if num > 8:
        break

    if num % 4 == 0:
        num += 1
        continue

    print(num)

    num += 1

# ==========================================
# Key Learnings:
#
# break:
# - exits the immediate loop completely
#
# continue:
# - skips current iteration
# - moves control to next iteration
#
# while True:
# - creates infinite loop
# - usually controlled using break
#
# Important:
# Always update variable before continue
# otherwise infinite loop may happen
# ==========================================
# Key Learnings:
# - while loop needs:
#   1. initialization
#   2. condition
#   3. update
#
# - Truthy values keep loop running
# - break stops loop
# - continue skips current iteration
# - indexing helps traverse strings
# - increment/decrement controls flow
# ==========================================