# ==========================================
# PYTHON EXCEPTION HANDLING – SOLUTIONS
# ==========================================

# ------------------------------------------
# 1️⃣ Safe List Index Access


numbers = [10, 20, 30, 40, 50]

try:

    index = int(input("Enter index number: "))

    print("Value:", numbers[index])

except IndexError:

    print("Index does not exist in the list")

except ValueError:

    print("Please enter a valid number")

# ------------------------------------------
# 2️⃣ Student Marks Dictionary Program

marks = {
    "maths": 80,
    "science": 70,
    "english": 65
}

try:

    subject = input("Enter subject name: ")

    print("Marks:", marks[subject])

except KeyError:

    print("Subject not found in dictionary")

# ------------------------------------------
# 3️⃣ Shopping Cart Bill Splitter

cart = [120, 340, 560, 200]

try:

    total = 0

    for item in cart:
        total += item

    people = int(input("Enter number of people: "))

    print("Each person pays:", total / people)

except ZeroDivisionError:

    print("Number of people cannot be zero")

except ValueError:

    print("Please enter valid number")

# ------------------------------------------
# 4️⃣ Word Counter Program

try:

    sentence = input("Enter sentence: ")

    words = sentence.split()

    print("Total words:", len(words))

except Exception as e:

    print("Something went wrong:", e)

# ------------------------------------------
# 5️⃣ Safe File Reader

try:

    filename = input("Enter filename: ")

    file = open(filename, "r")

    content = file.read()

    print(content)

    file.close()

except FileNotFoundError:

    print("File does not exist")

finally:

    print("Program finished")

# ------------------------------------------
# 6️⃣ Student Database Lookup

students = {
    "Shivam": 85,
    "Rahul": 72,
    "Aman": 90
}

try:

    name = input("Enter student name: ")

    print("Marks:", students[name])

except KeyError:

    print("Student not found in database")

# ------------------------------------------
# 7️⃣ Simple Login System

username = "admin"
password = "1234"

try:

    user = input("Enter username: ")

    pwd = input("Enter password: ")

    if user == username and pwd == password:

        print("Login successful")

    else:

        raise Exception("Invalid credentials")

except Exception as e:

    print(e)

# ------------------------------------------
# 8️⃣ ATM Withdrawal System

balance = 5000

try:

    withdraw = int(input("Enter withdrawal amount: "))

    if withdraw > balance:

        raise Exception("Insufficient balance")

    balance -= withdraw

    print("Remaining balance:", balance)

except ValueError:

    print("Please enter valid amount")

except Exception as e:

    print(e)

# ------------------------------------------
# 9️⃣ Largest Number from List

numbers = [10, 50, 90, 30]

try:

    print("Largest number:", max(numbers))

except ValueError:

    print("List is empty")

# ------------------------------------------
# 🔟 File Writer Program

try:

    text = input("Enter text to save: ")

    file = open("data.txt", "w")

    file.write(text)

    file.close()

    print("Data saved successfully")

except Exception as e:

    print("Error occurred:", e)

finally:

    print("Program ended")

# ==========================================
# KEY LEARNINGS
# ==========================================

# try:
# risky code goes here

# except:
# handles errors safely

# finally:
# always executes

# raise:
# creates custom exception manually

# Common Exceptions:
# ValueError
# IndexError
# KeyError
# ZeroDivisionError
# FileNotFoundError

# Exception as e:
# stores actual error message

# Exception handling prevents
# program from crashing
# ==========================================

