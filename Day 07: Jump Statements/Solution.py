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