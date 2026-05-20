# Polymorphism: Same functions but with different Behaviour
# - Method Overriding - only support in Python
# - Method Overloading - doesn't support in python, but in Java

# Example:
# Person: Behaviour: Run
# Engine: Behaviour: Run
# Code: Behaviour: Run

# Same word -> Different Behaviour



class Testing:
    
    # Method Overriding
    def polyfunction(self):
        print("the first function")
        
    def polyfunction(self):
        print("The second function")
        
    def polyfunction(self): # Method Overriding
        print("The third function")  
     
    # Method Overloading   
    def overloading(self, name):
        print(f"This is the {name}")
    
    def overloading(self, name, age):
        print(f"this is having {name} and {age}")  
        
    def add(self,*numbers):
        sum = 0
        for i in numbers:
            sum = i + sum
        return sum           
        

t = Testing()
t.polyfunction() 
# ---> polyfunction(t)
t.overloading("Gaurav",30)
a = Testing()
print("this is addition", a.add(2,3))
print("this is addition", a.add(4,5,6,7,8))

class Teacher:
    def show(self):
        print("I am a teacher")


class Student:
    def show(self):
        print("I am a student")
                    
        
        
# s = Student()
# t = Teacher()

# s.show()
# t.show()      

school_obj_details = [Student(), Teacher()] 

for sod in school_obj_details:
    sod.show()   
    

    
    
        