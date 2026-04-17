# Every program should go through 4 stages:
# 1. Understand the problem.
# 2. Write the logic in simple language
# 3. Convert logic into step-by-step actions
# 4. Convert steps into python

# Program to print 1 to 10
# 1. Start should be 1 and end should be 10 -> a = 1, <= 10
# 2. print karna hai -> print()
# 3. We can use loop or by default manually print -> while
# 4. increment value after each iteration -> a = a + 1

# a = 1
# while a <= 10:
#     print(a)
#     a = a + 1


# Print only odd values from 1 to 20 

# 1. print -> start=1 - end=20 -> a = 1, <=20
# 2. While end <=20 -> while a <= 20
# 3. print only when iteration is at odd -> if statement a%2 != 0
# 4. increment or should be outside the condition -> a += 1 


a = 1
while a <=20:
    if a%2 != 0:
        print(a)
    a += 1    
    