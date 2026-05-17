# ==========================================
# STRING LOGIC PROGRAMS – SOLUTIONS
# ==========================================

# ==========================================
# 🟢 Level 1 – Basic Loop + Condition
# ==========================================

# ------------------------------------------
# 1️⃣ Count Vowels

text = input("Enter string: ")

count = 0

for ch in text:

    if ch.lower() in "aeiou":
        count += 1

print("Total vowels:", count)

# ------------------------------------------
# 2️⃣ Count Consonants

text = input("Enter string: ")

count = 0

for ch in text:

    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1

print("Total consonants:", count)

# ------------------------------------------
# 3️⃣ Count Uppercase & Lowercase


text = input("Enter string: ")

upper = 0
lower = 0

for ch in text:

    if ch.isupper():
        upper += 1

    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

# ------------------------------------------
# 4️⃣ Count Digits

text = "abc123xyz45"

count = 0

for ch in text:

    if ch.isdigit():
        count += 1

print("Total digits =", count)

# ------------------------------------------
# 5️⃣ Count Spaces

text = input("Enter sentence: ")

count = 0

for ch in text:

    if ch == " ":
        count += 1

print("Total spaces:", count)

# ------------------------------------------

# ==========================================
# 🟡 Level 2 – Character Checking Logic
# ==========================================

# ------------------------------------------

# 6️⃣ Print Only Vowels

text = "education"

for ch in text:

    if ch in "aeiou":
        print(ch, end=" ")

print()

# ------------------------------------------
# 7️⃣ Print Characters at Even Index

text = input("Enter string: ")

for i in range(len(text)):

    if i % 2 == 0:
        print(text[i])

# ------------------------------------------
# 8️⃣ Reverse String Without Slicing

name = "pradyumna"

index = len(name) - 1

while index >= 0:

    print(name[index], end="")

    index -= 1

print()

# ------------------------------------------
# 9️⃣ Check Palindrome

text = input("Enter string: ")

reverse = ""

index = len(text) - 1

while index >= 0:

    reverse += text[index]

    index -= 1

if text == reverse:
    print("Palindrome")

else:
    print("Not Palindrome")

# ------------------------------------------
# 🔟 Find First Non-Repeating Character

text = "aabbcdd"

for ch in text:

    if text.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
    
# ------------------------------------------

# ==========================================
# 🟠 Level 3 – Pattern Logic Using Strings
# ==========================================

# ------------------------------------------

# 1️⃣1️⃣ Remove All Vowels

text = "python"

result = ""

for ch in text:

    if ch not in "aeiou":
        result += ch

print(result)

# ------------------------------------------
# 1️⃣2️⃣ Replace Space With "-"

text = "Python is powerful"

result = ""

for ch in text:

    if ch == " ":
        result += "-"

    else:
        result += ch

print(result)

# ------------------------------------------
# 1️⃣3️⃣ Count Frequency of Each Character

text = "banana"

checked = ""

for ch in text:

    if ch not in checked:

        print(ch, "=", text.count(ch))

        checked += ch

# ------------------------------------------
# 1️⃣4️⃣ Find Longest Word in Sentence

sentence = "Python is very powerful language"

words = sentence.split()

longest = words[0]

for word in words:

    if len(word) > len(longest):
        longest = word

print(longest)

# ------------------------------------------
# 1️⃣5️⃣ Lowercase to Uppercase Without upper()

text = "python"

result = ""

for ch in text:

    result += chr(ord(ch) - 32)

print(result)

# ------------------------------------------

# ==========================================
# 🔵 Level 4 – Logical Thinking Problems
# ==========================================

# ------------------------------------------

# 1️⃣6️⃣ Check Anagram

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("Anagram")

else:
    print("Not Anagram")

# ------------------------------------------
# 1️⃣7️⃣ Remove Duplicate Characters

text = "programming"

result = ""

for ch in text:

    if ch not in result:
        result += ch

print(result)

# ------------------------------------------
# 1️⃣8️⃣ Count Words Without split()

sentence = "Python is very powerful"

count = 1

for ch in sentence:

    if ch == " ":
        count += 1

print("Total words:", count)

# ------------------------------------------
# 1️⃣9️⃣ Compress String


text = "aaabbc"

result = ""

count = 1

for i in range(len(text)-1):

    if text[i] == text[i+1]:

        count += 1

    else:

        result += text[i] + str(count)

        count = 1

result += text[-1] + str(count)

print(result)

# ------------------------------------------
# 2️⃣0️⃣ Find Second Most Frequent Character

text = "banana"

frequency = {}

for ch in text:

    frequency[ch] = text.count(ch)

values = list(frequency.values())

values.sort(reverse=True)

second_highest = values[1]

for key, value in frequency.items():

    if value == second_highest:
        print("Second most frequent character:", key)
        break

# ==========================================
# KEY LEARNINGS
# ==========================================

# isalpha() --> checks alphabet

# isdigit() --> checks digit

# isupper() --> checks uppercase

# islower() --> checks lowercase

# ord() --> gives ASCII value

# chr() --> converts ASCII to character

# count() --> counts occurrence

# split() --> converts sentence into words

# sorted() --> sorts characters

# String logic improves:
# - problem solving
# - loop understanding
# - condition handling
# ==========================================