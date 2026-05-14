# Functions -> which performs some functionality
#  - Primary responsibility of function: Capability of reusability
#  - It has definition and calling
#  - Definition -> Defines the functionality of the function
#  - Calling -> calles the functionality

# perform task 1
# perform task 2
# 1000 lines between this
# perform task 1


print("Welcome to the class")
# print(a) NameError: name 'a' is not defined
# pythonsession() NameError: name 'pythonsession' is not defined

#Example 1: Creating a custom function
def greet():
    print("Welcome to python class")
    
greet()   
greet()  
greet()

#Example 2: Parameters/Arguements
def greet(name): # Parameter
    print("Welcome to python class", name)
    
a = "Nishchal"    
greet(a)   #arguement
greet("Akanksha") #arguement
  


#Example 3: Failure Scenarios
def add(a,b): # Parameter
    print(a+b)
    
# add(2) # TypeError: add() missing 1 required positional argument: 'b'
# add(6,"String") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
add("Thank", " You") # Thank You 


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


