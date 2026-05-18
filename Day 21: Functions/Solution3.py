# ==========================================
# __name__ and "__main__" – SOLUTIONS
# ==========================================

# ==========================================
# Step 1: Basic File Execution
# ==========================================

# file1.py

print("Inside file1")

print("Value of __name__:", __name__)

# Run:
# python file1.py

# Output:
# Inside file1
# Value of __name__: __main__

# Explanation:
# When a Python file runs directly,
# Python sets __name__ == "__main__"
# ------------------------------------------

# ==========================================
# Step 2: Import Behavior
# ==========================================

# file1.py

print("Inside file1")

print("Value of __name__:", __name__)

# ==========================================

# main.py

import file1

# Run:
# python main.py

# Output:
# Inside file1
# Value of __name__: file1

# Explanation:
# When imported,
# __name__ becomes filename
# ------------------------------------------

# ==========================================
# Step 3: Add Function + Execution
# ==========================================

# file1.py

print("Start of file1")

def greet():

    print("Hello from greet function")

greet()

print("End of file1")

# ==========================================

# main.py

import file1

# Run:
# python main.py

# Output:
# Start of file1
# Hello from greet function
# End of file1

# Explanation:
# Entire file executes during import
# greet() runs automatically
# because it is called directly
# ------------------------------------------

# ==========================================
# Step 4: Problem Scenario
# ==========================================

# file1.py

def add(a, b):

    return a + b

print("Adding:", add(2, 3))

# ==========================================

# main.py

import file1

print("Main running")

# Run:
# python main.py

# Output:
# Adding: 5
# Main running

# Explanation:
# Python executes all top-level code
# during import
# ------------------------------------------

# ==========================================
# Step 5: Using __name__
# ==========================================

# file1.py

def add(a, b):

    return a + b

if __name__ == "__main__":

    print("Adding:", add(2, 3))

# ==========================================

# main.py

import file1

print("Main running")

# Run:
# python main.py

# Output:
# Main running

# Explanation:
# add(2,3) did not execute
# because file1 was imported
# and __name__ became "file1"
# ------------------------------------------

# ==========================================
# Step 6: Direct Execution Check
# ==========================================

# Run:
# python file1.py

# Output:
# Adding: 5

# Explanation:
# When file1.py runs directly,
# __name__ becomes "__main__"

# Condition becomes True
# ------------------------------------------

# ==========================================
# Step 7: Execution Flow
# ==========================================

# file1.py

print("Line 1")

if __name__ == "__main__":

    print("Line 2")

print("Line 3")

# ==========================================

# main.py

import file1

# Run:
# python main.py

# Output:
# Line 1
# Line 3

# Explanation:
# Line 2 skipped
# because file was imported
# ------------------------------------------

# ==========================================
# Step 8: With Function Call
# ==========================================

# file1.py

def greet():

    print("Hello from greet")

if __name__ == "__main__":

    greet()

# ==========================================

# main.py

import file1

file1.greet()

# Run:
# python main.py

# Output:
# Hello from greet

# Explanation:
# greet() runs only once
# because:
# imported file skipped __main__ block
# but main.py called greet() manually
# ------------------------------------------

# ==========================================
# Step 9: Debug File Location
# ==========================================

# main.py

import file1

print("Imported from:", file1.__file__)

# Run:
# python main.py

# Output Example:
# Imported from:
# C:/PythonProjects/file1.py

# Explanation:
# __file__ gives complete path
# of imported file

# ------------------------------------------

# ==========================================
# Step 10: Final Understanding Test
# ==========================================

# file1.py

print("A")

if __name__ == "__main__":

    print("B")

print("C")

# ==========================================

# main.py

import file1

# Run:
# python main.py

# Output:
# A
# C

# Explanation:
# A printed normally
# B skipped because imported
# C printed normally

# ==========================================
# FINAL TAKEAWAY
# ==========================================

# __name__ == "__main__"
# when file runs directly

# __name__ == "filename"
# when imported

# if __name__ = "__main__":
# used to prevent automatic execution
# during import

# Helps:
# = reusable modules
# = clean imports
# = controlled execution

# Top-level code:
# executes automatically on import

# Best Practice:
# keep testing code inside:
# if __name__ == "__main__":
# ==========================================


