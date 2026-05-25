# Access Specifier:
# 1. Public -> rules
# 2. Private (__<variable>, __method()) -> 
# 3. Protected (_<variable>, _method()) -> convension


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.__age = age
        self._address = address
        
    def show(self):
        print("This is public method",self.name, self.__age, self._address)  
        
    def calculate_age(self):
        return self.__age
       
    def __private_show(self):
        print("this is private method: ",self.name, self.__age) 
      
    def internal_call(self):
        self.__private_show()       


class ChildClass(Student):  
    _ChildClass__age = 12 
    
    def child_jump_method(self):
        # print(self.__age)
        # print(self._ChildClass__age) Name Mangling
        self.__private_show()        

s1 = Student("Gungun", 25, "Bhopal")
# print(s1.name, s1.__age) // Private variable
s1.show()
print(s1._address)
# s1.__private_show() // Private method calling
s1.internal_call()   
print(s1.calculate_age() ) 

c1 = ChildClass("Rahul", 24, "Delhi")
# c1.child_jump_method() 
print(c1.calculate_age() ) 


# Purpose of Access Specifier
# - Protect the sensitive data
# - Control access of the data