# Perfect—this is where real understanding of Python starts. I’ll solve each one with **step-by-step logic**, not just answers.


# 1️⃣ Arithmetic + Precedence

a = 8
b = 3
c = 2

print(a + b * c - a // b)

## ✅ Step-by-step (operator precedence)

# Order:

# 1. `*` and `//`
# 2. `+` and `-`

### Step 1: Multiplication

b * c = 3 * 2 = 6

### Step 2: Floor Division

a // b = 8 // 3 = 2

# 👉 `//` means **floor division** → removes decimal → 2.66 → 2

### Step 3: Final expression


a + 6 - 2 = 8 + 6 - 2 = 12

## ✅ Output:

12

# 2️⃣ Arithmetic (Mix Operations)


x = 10
y = 4

print(x % y + x // y * 2)

## ✅ Step-by-step

### Step 1: Modulus


x % y = 10 % 4 = 2


# 👉 `%` gives **remainder**

### Step 2: Floor division


x // y = 10 // 4 = 2


### Step 3: Multiplication

2 * 2 = 4

### Step 4: Addition

2 + 4 = 6

## ✅ Output:

6

# 3️⃣ Logical Operator (Truthy/Falsy)

print("" or 0 or False or "Python")
print("Hello" and "World")


## ✅ First line


"" or 0 or False or "Python"


# 👉 Python checks left → right
# Returns **first truthy value**

# * `""` → False
# * `0` → False
# * `False` → False
# * `"Python"` → True ✅

## Output:

"Python"

## ✅ Second line

"Hello" and "World"

# 👉 `and` returns **last value if all are True**

# * `"Hello"` → True
# * `"World"` → True

## Output:

"World"

## 🧠 Why not True/False?

# Python returns **actual value**, not just boolean.


# 4️⃣ Comparative + Logical

a = 5
b = 10
c = 5

print(a == c and b > a or b == c)

## ✅ Step-by-step

### Step 1: Comparisons

a == c # → 5 == 5 → True
b > a # → 10 > 5 → True
b == c # → 10 == 5 → False

### Step 2: Logical precedence

# Order:

# 1. `and`
# 2. `or`

### Step 3:

True and True # → True
True or False # → True


## ✅ Output:

True

# 5️⃣ Logical + `not`

print(not 0)
print(not "Hello")
print(not "")

## ✅ Evaluate one by one

### 1. `not 0`

# `0` → False
# `not False` → True

# 👉 Output:

True

### 2. `not "Hello"`

#  Non-empty string → True
#  `not True` → False

# 👉 Output:

False

### 3. `not ""`

#  Empty string → False
#  `not False` → True

# 👉 Output:

True

# 🧠 Truthy vs Falsy (Core Concept)

## ❌ Falsy values:

# * `0`
# * `""` (empty string)
# * `False`
# * `None`

## ✅ Truthy:

# * Any non-zero number
# * Any non-empty string


# 🔥 Final Insight (Very Important)

# * `or` → returns **first True value**
# * `and` → returns **last value if all True**
# * `not` → flips True ↔ False

