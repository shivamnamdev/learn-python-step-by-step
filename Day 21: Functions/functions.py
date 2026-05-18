# Functions -> which performs some functionality
#  - Primary responsibility of function: Capability of reusability
#  - It has definition and calling
#  - Definition -> Defines the functionality of the function
#  - Calling -> calls the functionality

# perform task 1
# perform task 2
# 1000 lines between this
# perform task 1

# Naming Convension
# Java -> To add two values -> addTwoValues()
# Python -> To add two values -> add_two_values()

print("Welcome to the class")
# print(a) NameError: name 'a' is not defined
# pythonsession() NameError: name 'pythonsession' is not defined

#Example 1: Creating a custom function
def greet():  # Definition a function
    print("Welcome to python class")
    
greet()   # Calling a function
greet()  
greet()

#Example 2: Parameters/Arguements
def welcome(name): # Parameter
    print("Welcome to python class", name)
    
a = "Nishchal"    
welcome(a)   #arguement
welcome("Akanksha") #arguement
  


#Example 3: Failure Scenarios
def add(a,b): # Parameter
    print(a+b)
    
# add(2) # TypeError: add() missing 1 required positional argument: 'b'
# add(6,"String") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
add("Thank", " You") # Thank You 
add(2,5)


# Example 4: Returning the value
def add(a,b): # Parameter
    return a+b

a = add(3,7)
print(a)


print(add(5,8))




# Program

def print_marks(data):
    for subject in data:
        print(subject, ":", data[subject] )

marks = {
    "maths": 80,
    "science": 75
}

print_marks(marks)

# Global vs Local Variable

x = 10  # Global Variable

def show(z): # Parameter/Local Variable
    # x = 40  # Also a Local Variable
    # globals()['x'] = 40  # Another way of introducing global variable
    global x
    x = 40  # global variable
    y = 20  # Local Variable
    print(x+y+z)
    
print(x)    
show(30)  
print(x)  

def send_notification(name, number, type, date, address, bonus, contact):
    message = f"Dear {name} Your {number}{type}service is due on {date} Visit {address} for best service and amazing {bonus}. Call {contact} for details. KUNDAN HYUNDAI"
    print(message)


send_notification("Nishchal", "2nd", "free", "today", "Our Service Center", "benefits", "98728395234")


# Arbitrary Functions

# 1. *args -> way to get the unlimited values
# 2. **kwargs -> way to get the unlimited key-values

def add(*numbers):
    print(type(numbers))
    total = 0
    for n in numbers:
        total += n
    print(total)
    
add(1,2,3,4,5)
add(1,5,2) 
add(1) 
# add([1,3,5],[9,1,3]) would also fine


def student(**data):
    print(data)
    print(data)
    
student(name="Mahak", age=29, city="Dublin") 
student(id=101, Designation="Security Analyst")   


# Default Parameter

def add(a=2,b=5,c=7):
    return a+b+c

print(add(3,6)) # 9
print(add())    # 7
print(add(4))   # 9
print(add(c=4)) # 6


