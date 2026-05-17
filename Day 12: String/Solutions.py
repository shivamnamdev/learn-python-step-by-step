# ==========================================
# STRING INDEXING & SLICING – SOLUTIONS
# ==========================================

# ==========================================
# 🟢 Level 1: Basic Indexing Practice
# ==========================================

# ------------------------------------------
# Print first character

text = "Programming"

print(text[0])

# ------------------------------------------
# Print last character using negative indexing

text = "Programming"

print(text[-1])

# ------------------------------------------
# Print 4th character

text = "Programming"

print(text[3])

# ------------------------------------------
# Print second last character

text = "Programming"

print(text[-2])

# ------------------------------------------
# Print last character from user input
# 

text = input("Enter text: ")

print(text[-1])

# ------------------------------------------

# ==========================================
# 🟡 Level 2: Basic Slicing
# ==========================================

# ------------------------------------------

# Print "Python"

word = "PythonDeveloper"

print(word[0:6])

# ------------------------------------------
# Print "Developer"

word = "PythonDeveloper"

print(word[6:15])

# ------------------------------------------
# Print "thon"

word = "PythonDeveloper"

print(word[2:6])

# ------------------------------------------
# Print first 5 characters

word = "PythonDeveloper"

print(word[:5])

# ------------------------------------------
# Print last 4 characters

word = "PythonDeveloper"

print(word[-4:])

# ------------------------------------------

# ==========================================
# 🟠 Level 3: Step Slicing
# ==========================================

# ------------------------------------------

# Print every second character

data = "ABCDEFGHIJK"

print(data[::2])

# ------------------------------------------
# Print every third character

data = "ABCDEFGHIJK"

print(data[::3])

# ------------------------------------------
# Print index 1 to 8 with step 2

data = "ABCDEFGHIJK"

print(data[1:8:2])

# ------------------------------------------
# Print entire string using slicing

data = "ABCDEFGHIJK"

print(data[:])

# ------------------------------------------
# Print reverse string

data = "ABCDEFGHIJK"

print(data[::-1])

# ------------------------------------------

# ==========================================
# 🔵 Level 4: Reverse Logic Thinking
# ==========================================

# ------------------------------------------

# Print "Python" using negative slicing

text = "LearningPython"

print(text[-6:])

# ------------------------------------------
# Print "gninraeL"

text = "LearningPython"

print(text[7::-1])

# ------------------------------------------
# Print "nohtyP"

text = "LearningPython"

print(text[:-7:-1])

# ------------------------------------------
# Print characters from index 10 to 4 reverse

text = "LearningPython"

print(text[10:4:-1])

# ------------------------------------------
# Reverse string without [::-1]


text = "LearningPython"

index = len(text) - 1

while index >= 0:

    print(text[index], end="")

    index -= 1

print()

# ------------------------------------------

# ==========================================
# 🔥 Bonus Thinking Questions
# ==========================================

# ------------------------------------------

# Print "Day-10"

sentence = "Today is Day-10"

print(sentence[9:15])

# ------------------------------------------
# Print "Today" in reverse

sentence = "Today is Day-10"

print(sentence[4::-1])

# ------------------------------------------
# Print "is"

sentence = "Today is Day-10"

print(sentence[6:8])

# ------------------------------------------
# Print every second character

sentence = "Today is Day-10"

print(sentence[::2])

# ------------------------------------------
# Predict output

sentence = "Today is Day-10"

print(sentence[-1:-6:-1])


# ==========================================
# KEY LEARNINGS
# ==========================================

# Indexing:
# accesses single character

# Positive Index:
# starts from left
# 0,1,2,3...

# Negative Index:
# starts from right
# -1,-2,-3...

# Slicing:
# string[start:end]

# Step slicing:
# string[start:end:step]

# Reverse:
# string[::-1]

# Shortcut:
# [:] --> full string
# [:5] --> first 5 chars
# [-4:] --> last 4 chars

# Slicing end index is excluded
# ==========================================