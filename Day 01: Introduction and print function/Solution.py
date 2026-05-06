# Great—this is exactly the kind of **Day 1 reinforcement** that builds strong basics. I’ll give you clean solutions + what you should observe.


# 🟢 Level 1: Basic Practice

## 1. Print your name

print("Shivam Namdev")

## 2. Print your school or college name

print("Your College Name")

## 3. Print your favorite quote

print("Success is the result of consistent effort.")


# 🟠 Level 2: Experimentation

## 4. Print your age

print(30)

# 👉 You can also write:

print("30")

# (Both work, but one is a number, one is a string)


## 5. Print your name and age in one line

### Method 1 (comma separated)

print("Shivam Namdev", 30)

### Method 2 (string concatenation)

print("Shivam Namdev " + str(30))

### Method 3 (best practice – f-string)

print(f"Shivam Namdev is 30 years old")

## 6. Remove quotes and observe error

### ❌ Code:

print(Shivam)

### 🔴 Error:

# NameError: name 'Shivam' is not defined


## 🧠 Why this happens

# Python thinks:

# Shivam


# is a **variable name**, not text.

# Since you never created:

Shivam = "something"


# 👉 Python throws **NameError**

# 🔥 Key Learning from Day 1

# * `"text"` → string (safe)
# * without quotes → variable (must be defined)
# * `print()` → displays output
# * `,` vs `+` vs `f""` → different ways to combine data
