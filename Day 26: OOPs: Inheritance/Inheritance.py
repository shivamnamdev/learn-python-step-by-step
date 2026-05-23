# # Inheritance: One Class can use properties of another class.
# # Class Properties: Variables, Functions, Constructor
# # Purpose: So that Functions can be usable

# class Parent:
#     name = "Testing"
    
#     def __init__(self,*name):
#         self.name = name[0]
#         self.age = name[1]
        
#     def show(self):
#        print("This is the parent class")
       
# class Child(Parent):
#     def study(self):
#         print("This is child's study function")

# c = Child("Bacchan",36)
# c.show() 
# print(c.name, c.age)  

# # No parent can inherit from the child, But child can
# p = Parent("Sajan", 66)
# p.show()
# # p.study() AttributeError: 'Parent' object has no attribute 'study'

# Method Overriding with Inheritance

class Parent:
    name = "Testing"
    
    def __init__(self,*name):
        self.name = name[0]
        self.age = name[1]
        
    def show(self):
       print("This is the parent class")
       
class Child(Parent):
    def study(self):
        print("This is child's study function")
        
    def show(self):
        super().show()
        print("This is the child function")    

c = Child("Bacchan",36)
c.show() 
print(c.name, c.age)  

# p = Parent("Sajan", 66)
# p.show()
# # p.study()


# Types of Inheritance:
# Single: Parent -> Child
# Multi-Level: Grandparent -> Parent -> Child
# Multiple -> Child has more than 1 parent
# Heirarichal -> Parents has more than one child

# Benefit:
# Reduce the code duplicacy -> Code reusability
# Assess the Broader Functions
# Easy maintanance(Using the existing code)
# Cleaner structure
# Real-World Modeling


# Parent -> Base Functionality
# Child -> Specific Functionality

# Multi-Level Inheritance
class Animal:
    def eat(self):
        print("Animal eats")
        
class Dog(Animal):
    def bark(self):
        print("Dog Barks") 
        
class Puppy(Dog):
    def weep(self):
        print("puppy weeps")       
             
             
p = Puppy()
p.eat()
p.bark()
p.weep()               

# Multiple Inheritance

class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")    
        
class Child(Father, Mother):
    def skill3(self):
        # super().skills()
        print("coding")   
        
        
c = Child()
c.skill1()
c.skill2()  
c.skill3()      

    
# Heirarichal Inheritance
class Animal:
    def eat(self):
        print("Animal eats")
        
class Dog(Animal):
    def bark(self):
        print("Dog Barks")
        
class Cat(Animal):
    def meow(self):
        print("Cat Meow")                

c = Cat()
d = Dog()
c.eat()
d.eat()

c.meow()
d.bark()        