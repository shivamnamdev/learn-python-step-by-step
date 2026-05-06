# ================================
# Operators and Built-in Functions
# ================================

# 1. Take a name as input and print it
name = input("Enter your name: ")
print("Name:", name)

# --------------------------------

# 2. Take age as input and print value and type
age = input("Enter your age: ")
print("Age:", age)
print("Type of age:", type(age))  # always string

# --------------------------------

# 3. Take a number as input, convert it into integer, and print its type
num = input("Enter a number: ")
num = int(num)
print("Number:", num)
print("Type of number:", type(num))

# --------------------------------

# 4. Print the type of each variable
a = 10
b = 5.5
c = "Python"
d = True

print("Type of a:", type(a))  # int
print("Type of b:", type(b))  # float
print("Type of c:", type(c))  # str
print("Type of d:", type(d))  # bool

# --------------------------------

# 5. Membership operator (in)
print("Is 'a' in 'Python'? ->", "a" in "Python")   # False
print("Is 'Py' in 'Python'? ->", "Py" in "Python") # True

# --------------------------------

# 6. Observe 'is' with integers
a = 10
b = 10
print("a is b:", a is b)  # True (same memory for small integers)

# --------------------------------

# 7. Difference between == and is
a = [1, 2]
b = [1, 2]

print("a == b:", a == b)  # True (values same)
print("a is b:", a is b)  # False (different objects)

# --------------------------------

# 8. Difference between is not and !=
a = [1]
b = [1]

print("a != b:", a != b)        # False (values same)
print("a is not b:", a is not b) # True (different objects)

# --------------------------------

# 9. Identity for strings
s1 = "Python"
s2 = "Python"

print("s1 is s2:", s1 is s2)  # Usually True (string interning)

# --------------------------------

# 10. Check whether two variables point to same object
a = input("Enter value: ")
b = a

print("a is b:", a is b)  # True (same reference)

# --------------------------------

# Key Concepts:
# - input() always returns string
# - == compares values
# - is compares memory (object identity)
# - in checks membership
# - type() gives data type